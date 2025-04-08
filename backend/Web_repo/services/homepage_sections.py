from Web_repo.models.product import Products, Stores
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

def get_best_offers(limit=10, offset=0):
    products = Products.objects.order_by('-last_price_change_percentage')[offset:offset+limit]
    serializer = ProductSerializer(products, many=True)
    return serializer.data

def get_category_section(category_id, offset=0, limit=10):
    products = Products.objects.order_by('-last_price_change_percentage').filter(categories=category_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
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
    products = Products.objects.order_by('-last_price_change_percentage').filter(brand=brand_id)[offset:offset+limit] #.exclude(userfavorites__user_id=user) 
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

def get_top_offers_grouped_by_store():
    top_offers_by_store = defaultdict(list)
    products = Products.objects.order_by('-last_price_change_percentage').select_related('current_lowest_price__store_product_id__store_id')

    for product in products:
        if product.current_lowest_price and product.current_lowest_price.store_product_id:
            store = product.current_lowest_price.store_product_id.store_id
            top_offers_by_store[store.store_id].append(product)
    return top_offers_by_store

def get_homepage_section(user, section_index=0, inner_offset=0, inner_limit=10, section_limit=15, personalized_sections_limit=10):
    """
    Returns ONE section based on vertical index.
    """
    if section_index > section_limit:
        return None, False
    
    if section_index == 0:
        return {
            "id": "best_offers",
            "title": "Best Offers",
            "products": get_best_offers(limit=inner_limit, offset=inner_offset)
        }, True

    if user.is_authenticated:
        top_categories, top_brands = get_user_preferred_categories_and_brands(user, top_n= personalized_sections_limit//2)
        logging.debug(f"brands {top_brands}")
        
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
                return get_category_section(item_id, inner_offset, inner_limit), True
            else:
                return get_brand_section(item_id, inner_offset, inner_limit), True
        
    # After personalized ones, load store sections
    store_index_to_fetch = section_index - (1 + len(top_categories) + len(top_brands))
    top_offers_grouped = get_top_offers_grouped_by_store()
    store_ids = list(top_offers_grouped.keys())  

    if store_index_to_fetch < len(store_ids):
        store_id = store_ids[store_index_to_fetch]
        if store_id in top_offers_grouped:
            store = Stores.objects.get(store_id=store_id)
            products = top_offers_grouped[store_id]
            sorted_products = sorted(
                products,
                key=lambda p: p.current_lowest_price.price if p.current_lowest_price else float('inf')
            )
            product_serializer = ProductSerializer(sorted_products, many=True)
            return {
                "id": f"store_{store.store_id}",
                "title": f"Best from {store.name}",
                "icon": None,
                "products": product_serializer.data
            }, True
        else:
            return None, False
   

    return None, False

