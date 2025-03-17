from rest_framework import serializers
from .models import User, UserActivity, Products, Brand, PricesHistory, Currencys, StoreProducts, Stores, Categories, ProductCategory, ProductImage, UserHasLiked
from django.contrib.auth.hashers import make_password
from validate_email_address import validate_email

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Para ocultar la contraseña en la respuesta

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'password', 'date_of_birth', 'state']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        """Valida que el email tenga un dominio válido y pueda recibir correos"""
        if not validate_email(value, verify=True):
            raise serializers.ValidationError("El correo electrónico no es válido o no existe.")
        return value

    def create(self, validated_data):
        """Hashea la contraseña antes de guardar el usuario"""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)



class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    current_lowest_price = serializers.PrimaryKeyRelatedField(queryset=PricesHistory.objects.all())
    
    class Meta:
        model = Products
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class PricesHistorySerializer(serializers.ModelSerializer):
    currency_id = serializers.PrimaryKeyRelatedField(queryset=Currencys.objects.all())
    store_product_id = serializers.PrimaryKeyRelatedField(queryset=StoreProducts.objects.all())
    
    class Meta:
        model = PricesHistory
        fields = '__all__'


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


class ProductImageSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    
    class Meta:
        model = ProductImage
        fields = '__all__'


class UserHasLikedSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    
    class Meta:
        model = UserHasLiked
        fields = '__all__'
