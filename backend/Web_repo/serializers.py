from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from dns.resolver import resolve, NXDOMAIN, NoAnswer
from dns.exception import DNSException
from django.conf import settings
from django.template.loader import render_to_string
from .models import User, UserActivity, Products, Brand, PricesHistory, Currencys, StoreProducts, Stores, Categories, ProductCategory, ProductImage, UserHasLiked

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ocultar contraseña en la respuesta

    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'password', 'first_name', 'last_name', 
            'date_of_birth', 'state'
        ]
        extra_kwargs = {'password': {'write_only': True}, 'last_name': {'required': False},}

    def validate_email(self, value):
        """Valida que el email tenga un dominio válido y pueda recibir correos usando dnspython."""
        try:
            domain = value.split('@')[1]
            resolve(domain, 'MX')  # Verifica registros MX del dominio
        except (IndexError, NXDOMAIN, NoAnswer, DNSException):
            raise serializers.ValidationError("El correo electrónico no es válido o no existe.")
        return value

    def create(self, validated_data):
        # Asegúrate de que 'validated_data' esté bien definido
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)

        # Renderizar la plantilla HTML con el nombre completo del usuario
        html_message = render_to_string(
            'email/welcome_email.html',
            {
                'user': user,  # Aquí se pasa todo el objeto usuario
                'user_fullname': user.username,  # Nombre completo
                'website_url': 'https:google.com'  
            }
        )

        # Envío del correo de bienvenida en formato HTML
        send_mail(
            subject="¡Bienvenido a nuestra plataforma!",
            message="",  # Este campo puede quedar vacío cuando se envía html_message
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.username],
            fail_silently=False,
            html_message=html_message
        )

        return user




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
