from rest_framework import viewsets
from Web_repo.models.product import *
from Web_repo.serializers.product import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from collections import defaultdict
from django.utils import timezone
from datetime import timedelta

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
    

class ProductPriceHistoryChartView(APIView):
    def get(self, request):
        product_id = request.query_params.get('product_id')
        duration_param = request.query_params.get('duration')
        start_date = timezone.now() - timedelta(days=int(duration_param))
        if duration_param:
            start_date = timezone.now() - timedelta(days=int(duration_param))
                
        logging.debug(start_date)
        price_history_qs = PricesHistory.objects.filter(
            store_product_id__product_id=product_id,
            change_date__gte=start_date,
        ).select_related('store_product_id__store_id').order_by('change_date')

        
        store_data = defaultdict(list)

        for history in price_history_qs:
            store_name = history.store_product_id.store_id.name
            original_dt = history.change_date
            start_of_day_dt = original_dt.replace(hour=0, minute=0, second=0, microsecond=0)

            store_data[store_name].append({
                "x": start_of_day_dt.isoformat(),
                "y": history.price
            })


        
        datasets = []
        color_palette = ["#2B3695", "#6976EB", "#DD5144", "#ADB4F3", "#AA66CC"]

        for idx, (store, data_points) in enumerate(store_data.items()):
            datasets.append({
                "label": store,
                "data": data_points,
                "borderColor": color_palette[idx % len(color_palette)],
                "tension": 0.3,
                "fill": True
            })

        
        logging.debug(f"datasets {datasets}")
        return Response({
            "datasets": datasets
        })
    

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