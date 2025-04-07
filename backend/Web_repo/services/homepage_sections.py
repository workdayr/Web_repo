from Web_repo.models.product import Products, StoreProducts, PricesHistory, Stores
from Web_repo.models.user import UserFavorites
from collections import Counter, defaultdict
import logging

def get_user_preferred_categories_and_brands(user, top_n=3):
    favorites = UserFavorites.objects.filter(user_id=user).select_related('product_id__brand').prefetch_related('product_id__categories')

    category_counter = Counter()
    brand_counter = Counter()

    for fav in favorites:
        brand_counter[fav.product_id.brand] += 1
        for category in fav.product_id.categories.all():
            category_counter[category.category_id] += 1

    top_category_ids = [cat_id for cat_id, _ in category_counter.most_common(top_n)]
    top_brand_ids = [brand_id for brand_id, _ in brand_counter.most_common(top_n)]

    return top_category_ids, top_brand_ids

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

def get_best_offers(limit=10):
    products = Products.objects.order_by('-last_price_change')[:limit]
    serializer = ProductSerializer(products, many=True)
    return serializer.data


def get_dynamic_recommendation_sections(user, offset=0, limit=10):
    top_categories, top_brands = get_user_preferred_categories_and_brands(user)
    sections = []
    logging.debug(f"brands {top_brands} categoties {top_categories}")
    
    for i, category_id in enumerate(top_categories):
        products = Products.objects.order_by('-last_price_change').filter(categories=category_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
        if products.exists():
            category_name = products[0].categories.first().name # Assuming categories is a ManyToManyField
            serializer = ProductSerializer(products, many=True)
            sections.append({
                "id": f"cat_{category_id}",
                "title": f"From {category_name}",
                "icon": None,
                "products": serializer.data
            })

    for i, brand_id in enumerate(top_brands):
        products = Products.objects.order_by('-last_price_change').filter(brand=brand_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
        if products.exists():
            brand_name = products[0].brand.name
            serializer = ProductSerializer(products, many=True)
            sections.append({
                "id": f"brand_{brand_id}",
                "title": f"From {brand_name}",
                "icon": None,
                "products": serializer.data
            })
    
    return sections

def get_category_section(category_id, offset=0, limit=10):
    products = Products.objects.order_by('-last_price_change').filter(categories=category_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
    if products.exists():
        category_name = products[0].categories.first().name # Assuming categories is a ManyToManyField
        serializer = ProductSerializer(products, many=True)
        section = {
            "id": f"cat_{category_id}",
            "title": f"From {category_name}",
            "icon": None,
            "products": serializer.data
        }
        return section
    return None 

def get_brand_section(brand_id, offset=0, limit=10):
    products = Products.objects.order_by('-last_price_change').filter(brand=brand_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
    if products.exists():
        brand_name = products[0].brand.name
        serializer = ProductSerializer(products, many=True)
        section = {
            "id": f"brand_{brand_id}",
            "title": f"From {brand_name}",
            "icon": None,
            "products": serializer.data
        }
        return section
    return None 

def get_products_grouped_by_store_structured():
    sections = []
    products = Products.objects.order_by('-last_price_change').select_related('current_lowest_price')
    store_products_map = defaultdict(list)
    store_info_map = {}
    
    for product in products:
        if product.current_lowest_price:
            store_product = product.current_lowest_price.store_product_id
            store = store_product.store_id
            store_products_map[store.store_id].append(product)
            store_info_map[store.store_id] = {'id': store.store_id, 'name': store.name}

    for store_id, product_list in store_products_map.items():
        if store_id in store_info_map:
            store_data = store_info_map[store_id]
            sorted_products = sorted(
                product_list,
                key=lambda p: p.current_lowest_price.price if p.current_lowest_price else float('inf')
            )
            product_serializer = ProductSerializer(sorted_products, many=True)
            sections.append({
                "id": f"store_{store_data['id']}",
                "title": f"Best from {store_data['name']}",
                "icon": None,
                "products": product_serializer.data
            })

    return sections

def get_homepage_sections(user, page=0, per_section_limit=10):
    offset = page * per_section_limit
    sections = []

    if page == 0:
        # Static Top Best Offers
        sections.append({
            "id": "best_offers",
            "title": "Best Offers",
            "icon": None,
            "products": get_best_offers(limit=per_section_limit)
        })
    
    
    if user.is_authenticated:
        # Personalized Sections (From X / From Y)
        sections.extend(get_dynamic_recommendation_sections(user, offset=offset, limit=per_section_limit))

    # Grouped by store, loaded at any page    
    store_sections = get_products_grouped_by_store_structured()
    sections.extend(store_sections)

    return sections

def get_homepage_section(user, section_index=0, inner_offset=0, inner_limit=10, section_limit=15, personalized_sections_limit=10):
    """
    Returns ONE section based on vertical index.
    """
    if section_index > section_limit:
        return None
    
    if section_index == 0:
        return {
            "id": "best_offers",
            "title": "Best Offers",
            "products": get_best_offers(limit=inner_limit, offset=inner_offset)
        }

    if user.is_authenticated:
        top_categories, top_brands = get_user_preferred_categories_and_brands(user, top_n= personalized_sections_limit/2)
    
        index = section_index - 1  # offset from best offers
        
        # Interleave brands and categories
        interleaved = []
        min_length = min(len(top_brands), len(top_categories))
        
        # Add alternating brand/category pairs
        for i in range(min_length):
            interleaved.append(("brand", top_brands[i]))
            interleaved.append(("category", top_categories[i]))
        
        # Add remaining elements from whichever list is longer
        remaining_brands = [("brand", bid) for bid in top_brands[min_length:]]
        remaining_categories = [("category", cid) for cid in top_categories[min_length:]]
        
        all_ids = interleaved + remaining_brands + remaining_categories

        if index < len(all_ids):
            section_type, item_id = all_ids[index]
            if section_type == "category":
                return get_category_section(item_id, inner_offset, inner_limit)
            else:
                return get_brand_section(item_id, inner_offset, inner_limit)

    # After personalized ones, load store sections
    store_sections = get_products_grouped_by_store_structured()
    store_index = section_index - (1 + len(top_categories) + len(top_brands))
    if store_index < len(store_sections):
        return store_sections[store_index]

    return None

