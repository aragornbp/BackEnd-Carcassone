from django.urls import path
from .views import LoginJWTView, TokenObtainPairView, UserView, UserDetailView

urlpatterns = [
    path("login/", LoginJWTView.as_view()),
    path("token/refresh/", TokenObtainPairView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
