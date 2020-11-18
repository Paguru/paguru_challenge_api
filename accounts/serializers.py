from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.serializers import PostSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'posts']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']
