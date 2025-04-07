from rest_framework import serializers
from Web_repo.models.product import *
from django.db import transaction

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    
    class Meta:
        model = ProductImage
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    current_lowest_price = serializers.StringRelatedField()
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    current_lowest_price = serializers.PrimaryKeyRelatedField(queryset=PricesHistory.objects.all(), allow_null=True)

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self._context = kwargs.get('context', {})
        
        # Get extra_fields from kwargs or context
        self.extra_fields = kwargs.pop('extra_fields', []) or self._context.get('extra_fields', [])
        
        super().__init__(*args, **kwargs)
        
        if self.extra_fields:
            if 'primary_image_URL' in self.extra_fields:
                self.fields['primary_image_URL'] = serializers.SerializerMethodField()

            if 'images_URL' in self.extra_fields:
                self.fields['images_URL'] = serializers.SerializerMethodField()

            if 'brand_name' in self.extra_fields:
                self.fields['brand_name'] = serializers.CharField(source='brand.name', read_only=True, default=None)

            if 'current_lowest_price' in self.extra_fields:
                self.fields['current_lowest_price'] = PricesHistorySerializer(read_only=True)
        
    def get_primary_image_URL(self, obj):
        primary_image = obj.product_images.filter(is_primary=True).first()
        return primary_image.image_id.image_url if primary_image else None

    def get_images_URL(self, obj):
        return [
            product_image.image_id.image_url
            for product_image in obj.product_images.all()
            if product_image.image_id
        ]
    
    def get_current_lowest_price(self, obj):
        if obj.current_lowest_price:
            return obj.current_lowest_price.price
        return None

class PricesHistorySerializer(serializers.ModelSerializer):
    currency_id = serializers.PrimaryKeyRelatedField(queryset=Currencys.objects.all())
    store_product_id = serializers.PrimaryKeyRelatedField(queryset=StoreProducts.objects.all())
    
    class Meta:
        model = PricesHistory
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Override the create method to implement price change logic.
        """
        store_product = validated_data['store_product_id']
        new_price = validated_data['price']

        product = Products.objects.select_related(
            'current_lowest_price__store_product_id'
        ).get(pk=store_product.product_id.pk)

        current_lowest_price = product.current_lowest_price

        with transaction.atomic():
            # 2. Create the PriceHistory instance using the serializer's save()
            price_history = self.Meta.model(**validated_data)
            price_history.save()

            # 3. Get the product and update it
            should_update = False
            if current_lowest_price is None or new_price <= current_lowest_price.price or \
               current_lowest_price.store_product_id.store_id == store_product.store_id:
                product.last_price_change = (new_price - current_lowest_price.price) if current_lowest_price else 0
                product.current_lowest_price = price_history
                should_update = True

            if should_update:
              product.save(update_fields=['last_price_change', 'current_lowest_price'])

        return price_history

class CurrencysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencys
        fields = '__all__'


class StoreProductsSerializer(serializers.ModelSerializer):
    store_id = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    
    class Meta:
        model = StoreProducts
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    category_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())
    
    class Meta:
        model = ProductCategory
        fields = '__all__'
