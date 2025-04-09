from rest_framework import viewsets
from Web_repo.models.product import *
from Web_repo.serializers.product import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

import logging

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductDetailSerializer

class ProductDetailsView(APIView):
    def get(self, request):
        product_id = request.query_params.get('product_id')
        
        if not product_id:
            return Response({"error": "product_id parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = get_object_or_404(Products, product_id=product_id)
        except Products.DoesNotExist:
            return Response({"error": f"Product with id '{product_id}' not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid product_id format."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductDetailSerializer(product, context={'extra_fields':  ['images_URL', 'brand_name', 'current_lowest_price', 'store_name', 'store_image']})
        
        return Response(serializer.data)

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class PricesHistoryViewSet(viewsets.ModelViewSet):
    queryset = PricesHistory.objects.all()
    serializer_class = PricesHistorySerializer


class CurrencysViewSet(viewsets.ModelViewSet):
    queryset = Currencys.objects.all()
    serializer_class = CurrencysSerializer


class StoreProductsViewSet(viewsets.ModelViewSet):
    queryset = StoreProducts.objects.all()
    serializer_class = StoreProductsSerializer


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer