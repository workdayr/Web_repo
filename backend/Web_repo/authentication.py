from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.conf import settings

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        cookie_name = settings.SIMPLE_JWT.get("AUTH_COOKIE", "access_token")
        access_token = request.COOKIES.get(cookie_name)

        if not access_token:
            return None  # No token, proceed as unauthenticated

        try:
            # 2. Validate the token and get the user
            validated_token = self.get_validated_token(access_token)
            user = self.get_user(validated_token)
            return (user, validated_token)
            
        except InvalidToken as e:
            # 3. Handle invalid/expired tokens explicitly
            raise AuthenticationFailed("Invalid or expired token.") from e