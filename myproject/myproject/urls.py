from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskmanager.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
