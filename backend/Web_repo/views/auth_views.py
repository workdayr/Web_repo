from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from Web_repo.models import User
# authentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.conf import settings


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from Web_repo.serializers import *
import random

import logging

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
            logging.debug(f"From login Response cookies: {response.cookies}")
            
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
                logging.debug(e)
                return Response({"error": "Error during logout, please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Delete cookies
        response.set_cookie(
                key=settings.SIMPLE_JWT.get('AUTH_COOKIE', 'access_token'),
                value='',
                max_age = 0,
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

        # Set the new refresh token as an HTTP-only cookie
        response.set_cookie(
            key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
            value='',
            max_age=0,
            secure=settings.SIMPLE_JWT['REFRESH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['REFRESH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['REFRESH_COOKIE_SAMESITE']
        )

        logging.debug(response)
        return response

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT.get("AUTH_COOKIE_REFRESH", "refresh_token"))

        if not refresh_token:
            return Response({"error": "Refresh token missing"}, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        new_refresh_token = str(refresh)
        response = Response({"message":"Token refreshed"})
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
        
        return response
    

class UserAnalyticsView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        months_list = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]


        total_users = [190, 300, 500]
        registered_users = [0, 5,40,70 ,150, 160, 170, 200, 250, 300, 310, 320] 
        unregistered_users = [25,35, 23, 27,150, 170,130,300,310,200, 130,140 ]
        total_views = [200, 400, 600, 800,100,50,150,320,534,460,756,900]
        new_users = [60, 90, 120,100,50,150,320,534,460,756,900, 200]

        total_user_count = sum(total_users)
        total_registered_users = sum(registered_users)
        total_unregistered_users = sum(unregistered_users)
        total_new_signups = sum(new_users)

        months_count = months_count = min(len(months_list), len(months_list))
        total_users = total_users[-months_count:]
        registered_users = registered_users[-months_count:]
        unregistered_users = unregistered_users[-months_count:]
        total_views = total_views[-months_count:]
        new_users = new_users[-months_count:]

        data = {
            "months": months_list,
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
    

class NotificationAnalyticsView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        alert_data = {
            "on_time":[250,300,320,310,200,400,123],
            "days":["Mon", "Tue", "Wed",
                      "Thu", "Fri", "Sat", "Sun"]
        }
        total_on_time = sum(alert_data["on_time"])

        redirect_data = {
            "platforms": ["Amazon", "Mercado Libre", "AliExpress"],
            "redirect_count": [250, 180, 150,],
        }
        total_redirects = sum(redirect_data["redirect_count"])
        
        data = {
            "days": alert_data["days"],
            "onTimeAlerts": alert_data["on_time"],
            "totalOnTime": total_on_time,
            "platforms": redirect_data["platforms"],
            "redirectCounts":redirect_data["redirect_count"],
            "totalRedirects": total_redirects,
        }


        return Response(data)
    

class UserRecordView(APIView):
    def get(self, request, format=None):
        users = UserRecord.objects.all().order_by('-created_at')
        serializer = UserRecordSerializer(users, many = True)

        return Response(serializer.data)
    

    def delete(self, request, pk, format=None):
        print(f"Attempting to delete user with ID: {pk}")  # Debug print
        try:
            user = UserRecord.objects.get(pk=pk)
            print(f"Found user: {user.name}")  # Debug print
            user.delete()
            print("User deleted successfully")  # Debug print
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UserRecord.DoesNotExist:
            print(f"User with ID {pk} not found")  # Debug print
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error deleting user: {str(e)}")  # Debug print
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProductView(APIView):
    def get(self, request, format=None):
        # Generate simulated data if no products exist
        if not Product.objects.exists():
            self.generate_sample_products()
            
        products = Product.objects.all().order_by('-date')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def generate_sample_products(self):
        stores = ['Amazon', 'Mercado Libre', 'AliExpress']
        statuses = ['ongoing', 'ends_soon', 'ended']
        
        for i in range(1, 21):
            Product.objects.create(
                name=f"Product {i}",
                date=datetime.now() - timedelta(days=random.randint(0, 30)),
                status=random.choice(statuses),
                stores=random.sample(random.random(stores)),
                price=random.uniform(10, 1000)
            )
        
