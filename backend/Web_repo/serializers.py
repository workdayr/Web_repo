from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from dns.resolver import resolve, NXDOMAIN, NoAnswer
from dns.exception import DNSException
from django.conf import settings
from django.template.loader import render_to_string
from .models import *
import logging

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

<<<<<<< HEAD


class ProductsSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    current_lowest_price = serializers.PrimaryKeyRelatedField(queryset=PricesHistory.objects.all())
=======
class ProductImageSerializer(serializers.ModelSerializer):
    
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
>>>>>>> feature/client-auth
    
    class Meta:
        model = ProductImage
        fields = '__all__'

<<<<<<< HEAD
class NotificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = '__all__'
        
class RedirectAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedirectAnalytics
        fields = '__all__'

=======
>>>>>>> feature/client-auth
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    current_lowest_price = serializers.PrimaryKeyRelatedField(queryset=PricesHistory.objects.all(), allow_null=True)

    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self._context = kwargs.get('context', {})
        
        # Get extra_fields from kwargs or context
        self.extra_fields = kwargs.pop('extra_fields', []) or self._context.get('extra_fields', [])
        logging.debug(f'ProductsSerializer extra_fields: {self.extra_fields}')
        
        super().__init__(*args, **kwargs)
        
        if self.extra_fields:
            if 'primary_image_URL' in self.extra_fields:
                self.fields['primary_image_URL'] = serializers.SerializerMethodField()

            if 'images_URL' in self.extra_fields:
                logging.debug('Getting the images')
                self.fields['images_URL'] = ProductImageSerializer(many=True, source='product_images', read_only=True)

            if 'brand_name' in self.extra_fields:
                self.fields['brand_name'] = serializers.CharField(source='brand.name', read_only=True, default=None)

            if 'current_lowest_price' in self.extra_fields:
                self.fields['current_lowest_price'] = PricesHistorySerializer(read_only=True)
        
    def get_primary_image_URL(self, obj):
        primary_image = obj.product_images.filter(is_primary=True).first() 
        return primary_image.image_url if primary_image else None




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





class UserFavoritesSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = UserFavorites
        fields = '__all__'

<<<<<<< HEAD
class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecord
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    formatted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'formatted_date', 
                'status', 'stores', 'formatted_price']

    def get_product_id(self, obj):
        return f"#{obj.id:04d}"

    def get_formatted_date(self, obj):
        return obj.date.strftime("%b %d, %Y")

    def get_formatted_price(self, obj):
        return f"${obj.price:,.2f}"
=======
    def __init__(self, *args, **kwargs):
        # Get extra_fields from kwargs or use defaults
        extra_fields = kwargs.pop('extra_fields', ['primary_image_URL', 'brand_name', 'current_lowest_price'])
        
        super().__init__(*args, **kwargs)
        
        # Initialize product serializer safely
        self.fields['product'] = serializers.SerializerMethodField()
        self._extra_fields = extra_fields

    def get_product(self, obj):
        logging.debug(self._extra_fields)
        return ProductsSerializer(
            obj.product_id,
            context={'extra_fields': self._extra_fields}
        ).data


    
>>>>>>> feature/client-auth
