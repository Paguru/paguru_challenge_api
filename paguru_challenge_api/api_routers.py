  
from rest_framework import routers

# views sets imports
from accounts.viewsets import UserViewSet
from posts.viewsets import PostViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('posts', PostViewSet)

# export to urls
routes = router.urls
