from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, Q
from Web_repo.models import UserFavorites
from Web_repo.serializers import UserFavoritesSerializer
from Web_repo.authentication import CookieJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import logging


class UserFavoritesPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'pageSize'
    max_page_size = 100

class UserFavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = UserFavoritesSerializer
    pagination_class = UserFavoritesPagination
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = UserFavorites.objects.filter(user_id=user.user_id).select_related('product_id')
        
        sort_by = self.request.query_params.get('sortBy', 'liked_at')
        desc = self.request.query_params.get('desc', 'false').lower() == 'true'
        
        valid_sort_fields = ['liked_at', 'price_threshold', 'percentage_threshold']
        if sort_by not in valid_sort_fields:
            sort_by = 'liked_at'
            
        ordering = f"-{sort_by}" if desc else sort_by
        return queryset.order_by(ordering)
    
    def perform_create(self, serializer):
        logging.debug('from perform_create')
        logging.debug(self.request.user)
        logging.debug(self.request.user.user_id)
        serializer.save(user_id=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)