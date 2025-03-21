from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default='Marca Generica')


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default="Producto Generico")
    upc = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=2500)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    current_lowest_price = models.OneToOneField('PricesHistory', on_delete=models.CASCADE)

class PricesHistory(models.Model):
    price_history_id = models.AutoField(primary_key=True)
    price = models.IntegerField(null=False, blank=False, default=0)
    change_date = models.DateTimeField(auto_now=True)
    currency_id = models.ForeignKey('Currencys', on_delete=models.CASCADE, related_name="prices")
    store_product_id = models.ForeignKey('StoreProducts', on_delete=models.CASCADE, related_name="prices")


class Currencys(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=1)


class StoreProducts(models.Model):
    store_product_id = models.AutoField(primary_key=True)
    stock_keeping_unit = models.CharField(max_length=50, null=False, blank=False, default='Not known', unique=True)
    products_url = models.CharField(max_length=500)
    store_id = models.ForeignKey('Stores', on_delete=models.CASCADE, related_name="store_products")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="store_products")


class Stores(models.Model):
    Stores_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default="Tienda Generica")
    url = models.CharField(max_length=255, unique=True)
    search_url = models.CharField(max_length=255)
    custom_search_url = models.CharField(max_length=255)
    has_api = models.BooleanField(default=False)
    Image_url = models.CharField(max_length=500)


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=False, blank=False, default='Sin categoria')


class ProductCategory(models.Model):
    Product_category_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_categories")
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="product_categories")


class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_images")

'''
    USER MANAGEMENT
'''

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=256, null=False, blank=False)
    first_name = models.CharField(max_length=35, null=False)
    last_name = models.CharField(max_length=35, null=False)
    state = models.CharField(max_length=20, null=False, default='Unknown')
    date_of_birth = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Inherited from PermissionsMixin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class UserActivity(models.Model):
    user_activity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    last_login = models.DateTimeField(null=True, blank=True, default=None)
    ip_address = models.CharField(max_length=50, null=False)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.last_login if self.last_login else 'Nunca ha iniciado sesión'}"


class UserHasLiked(models.Model):
    user_has_liked_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="likes")
    liked_at = models.DateTimeField(auto_now_add=True)
