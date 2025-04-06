from django.db import models

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default='Marca Generica')
    
    def __str__(self):
        return self.name


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default="Producto Generico")
    upc = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=2500)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    current_lowest_price = models.ForeignKey('PricesHistory', on_delete=models.SET_NULL, null=True, blank=True)
    last_price_change = models.FloatField(null=True, blank=True) 
    
    def __str__(self):
        
        if self.current_lowest_price:
            return f"{self.name} - ${self.current_lowest_price.price}"
        return self.name
    def get_lowest_price(self, obj):
        """
        Obtiene el precio más bajo del producto buscando en PricesHistory
        """
        store_products = StoreProducts.objects.filter(product_id=obj)
        prices = PricesHistory.objects.filter(store_product_id__in=store_products).values_list('price', flat=True)

        return min(prices) if prices else None
    
class PricesHistory(models.Model):
    price_history_id = models.AutoField(primary_key=True)
    price = models.FloatField(null=False, blank=False, default=0)
    change_date = models.DateTimeField(auto_now=True)
    currency_id = models.ForeignKey('Currencys', on_delete=models.CASCADE, related_name="prices")
    store_product_id = models.ForeignKey('StoreProducts', on_delete=models.CASCADE, related_name="prices")
    
    def __str__(self):
        
        return f"Price: {self.price}, Date: {self.change_date.strftime('%Y-%m-%d %H:%M:%S')}"



class Currencys(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=1)
    
    def __str__(self):
        return self.currency


class StoreProducts(models.Model):
    store_product_id = models.AutoField(primary_key=True)
    stock_keeping_unit = models.CharField(max_length=50, null=False, blank=False, default='Not known')
    products_url = models.CharField(max_length=1500)
    store_id = models.ForeignKey('Stores', on_delete=models.CASCADE, related_name="store_products")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="store_products")
    
    def __str__(self):
        return f"{self.store_id} - {self.product_id}"


class Stores(models.Model):
    Stores_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default="Tienda Generica")
    url = models.CharField(max_length=255, unique=True)
    search_url = models.CharField(max_length=255)
    custom_search_url = models.CharField(max_length=255)
    has_api = models.BooleanField(default=False)
    Image_url = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name



class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=False, blank=False, default='Sin categoria')
    
    def __str__(self):
        return self.category


class ProductCategory(models.Model):
    Product_category_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_categories")
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="product_categories")


class Images (models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.image_name

class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    is_primary = models.BooleanField(default=False)
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE, related_name="Image",default=1)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product")
