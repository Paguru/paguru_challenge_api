from django.contrib import admin
from django.urls import path, include
from .api_routers import routes
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(routes)),
    path('api/v1/auth/', views.obtain_auth_token)
]
