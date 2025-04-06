from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from Web_repo.models.user import UserFavorites, User
from Web_repo.serializers.user import *
from Web_repo.authentication import CookieJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

import logging

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Sobreescribe create para enviar un correo de bienvenida al nuevo usuario."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer


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
        serializer.save(user_id=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'], url_path='remove-by-product')
    def remove_by_product(self, request):
        """Delete a favorite by product_id instead of the primary key"""
        product_id = request.query_params.get('product_id')

        if not product_id:
            return Response({'error': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        favorite = UserFavorites.objects.filter(user_id=request.user.user_id, product_id=product_id).first()

        if not favorite:
            return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)

        favorite.delete()
        return Response({'message': 'Favorite removed successfully'}, status=status.HTTP_204_NO_CONTENT)