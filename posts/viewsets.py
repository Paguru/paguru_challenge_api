from rest_framework import viewsets, permissions

from .serializers import PostSerializer
from .models import Post


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.author == request.user
        else:
            return False


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        self.permission_classes = [permissions.IsAuthenticated]
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthor]
        return super(self.__class__, self).get_permissions()
