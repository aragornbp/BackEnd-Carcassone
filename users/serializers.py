from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data.get("password"))
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}
