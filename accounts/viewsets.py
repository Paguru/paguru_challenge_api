from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions


from .serializers import UserSerializer, UserDetailSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.BasePermission()]
        else:
            return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserDetailSerializer
        return UserSerializer

