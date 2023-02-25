from django.urls import path
from .views import LoginJWTView, TokenObtainPairView

urlpatterns = [
    path("login/", LoginJWTView.as_view()),
    path("token/refresh/", TokenObtainPairView.as_view()),
]
