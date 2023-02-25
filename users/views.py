from .models import User
from .serializers import CustomJWTSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
