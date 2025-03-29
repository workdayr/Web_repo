"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Web_repo.views import *

# Crea un enrutador por defecto
router = DefaultRouter()

# Registra todos los viewsets en el router
router.register(r'users', UserViewSet)
router.register(r'users_activity', UserActivityViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'prices_history', PricesHistoryViewSet)
router.register(r'currencies', CurrencysViewSet)
router.register(r'store_products', StoreProductsViewSet)
router.register(r'stores', StoresViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'product_categories', ProductCategoryViewSet)
router.register(r'product_images', ProductImageViewSet)
router.register(r'user_likes', UserHasLikedViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # Accede a las rutas de los viewsets, por ejemplo, /api/users/
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/user_analytics/", UserAnalyticsView.as_view(), name="user_analytics"),
    path('api/notification_analytics/' , NotificationAnalyticsView.as_view(), name = 'notification_analytics'),
    path('api/user-records/', UserRecordView.as_view(), name = 'user-records'),
    path('api/user-records/<int:pk>/', UserRecordView.as_view(), name='user-records-detail'),
    path('api/product/', ProductView.as_view(), name='products-list'),
    path('api/product/<int:pk>/', ProductView.as_view(), name='products-detail'),
    
    ]
