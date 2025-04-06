from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Web_repo.models import User
# authentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.conf import settings




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
        try:
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
        except TokenError as e:
                # The refresh token is invalid or expired
                return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)