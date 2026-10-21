from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "date_joined", "avatar"]
        read_only_fields = ["date_joined"]

    def validate_username(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "Username must be greater then 2 characters !"
            )

        return value

    def validate_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be greater then 8 characters !"
            )

        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
