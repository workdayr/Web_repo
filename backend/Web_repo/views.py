from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from .models import User, UserActivity, Products, Brand, PricesHistory, Currencys, StoreProducts, Stores, Categories, ProductCategory, ProductImage, UserHasLiked
from .serializers import UserSerializer, UserActivitySerializer, ProductsSerializer, BrandSerializer, PricesHistorySerializer, CurrencysSerializer, StoreProductsSerializer, StoresSerializer, CategoriesSerializer, ProductCategorySerializer, ProductImageSerializer, UserHasLikedSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from rest_framework.authentication import TokenAuthentication
from Web_repo.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Sobreescribe create para enviar un correo de bienvenida al nuevo usuario."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Enviar correo de bienvenida
            '''
            send_mail(
                subject="¡Bienvenido a nuestra plataforma!",
                message=f"Hola {user.username}, gracias por registrarte en nuestra plataforma.",
                from_email="tu_correo@gmail.com",  # Reemplázalo con tu correo
                recipient_list=[user.email],
                fail_silently=False,
            )
            '''
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

        print(f"Checking login for email: {email}")  # Debugging

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            print(f"User found: {user}")  # Debugging
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            print("Authentication failed")  # Debugging
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserAnalyticsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

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