from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserDetail

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['bio', 'profile_picture', 'website']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user_password = validated_data.pop('password')
        new_user = User.objects.create(**validated_data)
        new_user.set_password(user_password)
        new_user.save()
        return new_user


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return {
            'user': user,
            'access': str(RefreshToken.for_user(user).access_token),
            'refresh': str(RefreshToken.for_user(user))
        }
