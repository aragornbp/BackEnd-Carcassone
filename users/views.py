from .models import User
from .serializers import CustomJWTSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
