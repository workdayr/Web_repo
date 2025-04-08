from rest_framework import serializers
from Web_repo.models.user import *
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from dns.resolver import resolve, NXDOMAIN, NoAnswer
from dns.exception import DNSException
from django.template.loader import render_to_string
from django.conf import settings
from Web_repo.serializers.product import ProductsSerializer

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


class UserFavoritesSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = UserFavorites
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        # Get extra_fields from kwargs or use defaults
        extra_fields = kwargs.pop('extra_fields', ['primary_image_URL','brand_name', 'current_lowest_price'])
        
        super().__init__(*args, **kwargs)
        
        # Initialize product serializer safely
        self.fields['product'] = serializers.SerializerMethodField()
        self._extra_fields = extra_fields

    def get_product(self, obj):
        return ProductsSerializer(
            obj.product_id,
            context={'extra_fields': self._extra_fields}
        ).data