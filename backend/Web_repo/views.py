from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User, UserActivity, Products, Brand, PricesHistory, Currencys, StoreProducts, Stores, Categories, ProductCategory, ProductImage, UserHasLiked
from .serializers import UserSerializer, UserActivitySerializer, ProductsSerializer, BrandSerializer, PricesHistorySerializer, CurrencysSerializer, StoreProductsSerializer, StoresSerializer, CategoriesSerializer, ProductCategorySerializer, ProductImageSerializer, UserHasLikedSerializer
from django.contrib.auth import authenticate

import logging
# authentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from datetime import datetime, timedelta
from django.conf import settings


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


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


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


class UserHasLikedViewSet(viewsets.ModelViewSet):
    queryset = UserHasLiked.objects.all()
    serializer_class = UserHasLikedSerializer

class LoginView(APIView):   
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"error": f"Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not User.objects.filter(email=email).exists():
            return Response({"error": f"User not found: {email}"}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(request, email=email, password=password)
        if user:
            user_data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            
            response = Response({"message": "Login successful", "user": user_data}, status=status.HTTP_200_OK)

            refresh = RefreshToken.for_user(user)
            response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                value = str(refresh.access_token),
                max_age = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
                value= str(refresh),  
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['REFRESH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['REFRESH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['REFRESH_COOKIE_SAMESITE']
            )
            logging.debug(f"Response cookies: {response.cookies}")
            
            return response

        return Response({"error": "Invalid credentials from authenticate function"}, status=status.HTTP_401_UNAUTHORIZED)


class RestoreSessionView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT.get('REFRESH_COOKIE', 'refresh_token'))
        logging.debug(f"Refresh token: {refresh_token}")
        if not refresh_token:
            return Response({"error": "No refresh token found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            new_refresh_token = str(refresh)  # Get the new refresh token

            response = Response({"message": "Session restored"}, status=status.HTTP_200_OK)

            # Set the new access token as an HTTP-only cookie
            response.set_cookie(
                key=settings.SIMPLE_JWT.get('AUTH_COOKIE', 'access_token'),
                value=access_token,
                max_age = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

            # Set the new refresh token as an HTTP-only cookie
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
                value=new_refresh_token,
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['REFRESH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['REFRESH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['REFRESH_COOKIE_SAMESITE']
            )

            # Getting user data
            try:
                user_id = refresh["user_id"]  # Extract user ID from token payload
                user = User.objects.get(user_id=user_id)
                user_data = {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
                response.data["user"] = user_data
                
            except Exception:
                return Response({"error": "Can't restore user data"}, status=status.HTTP_401_UNAUTHORIZED)

            return response

        except TokenError as e:
            # The refresh token is invalid or expired
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request): 
        response = Response({"message": "Logged out"}, status=status.HTTP_200_OK)

        # Get the refresh token from the cookies
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT.get('REFRESH_COOKIE', 'refresh_token'))
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except TokenError:
                response = Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": "Error during logout, please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Delete cookies
        response.delete_cookie(settings.SIMPLE_JWT.get('AUTH_COOKIE', 'access_token'))
        response.delete_cookie(settings.SIMPLE_JWT.get('REFRESH_COOKIE', 'refresh_token'))

        return response


class UserAnalyticsView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        current_month = datetime.now().strftime("%B")
        months_list = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        current_month_index = months_list.index(current_month)
        recent_months = months_list[max(0, current_month_index -3) : current_month_index +1]

        total_users = [190, 300, 500]
        registered_users = [150, 250, 420] 
        unregistered_users = [40, 50, 80]
        total_views = [200, 400, 600, 800]
        new_users = [60, 90, 120]

        total_user_count = sum(total_users)
        total_registered_users = sum(registered_users)
        total_unregistered_users = sum(unregistered_users)
        total_new_signups = sum(new_users)

        months_count = months_count = min(len(recent_months), len(total_users))
        total_users = total_users[-months_count:]
        registered_users = registered_users[-months_count:]
        unregistered_users = unregistered_users[-months_count:]
        total_views = total_views[-months_count:]
        new_users = new_users[-months_count:]

        data = {
            "months": recent_months,
            "totalUsers": total_users,
            "registeredUsers": registered_users,
            "unregisteredUsers": unregistered_users,
            "totalViews": total_views,
            "newUsers": new_users,
            "totalUserCount": total_user_count,
            "totalRegisteredUsers": total_registered_users,
            "totalUnregisteredUsers": total_unregistered_users,
            "totalNewSignups": total_new_signups,
        }

        return Response(data)
