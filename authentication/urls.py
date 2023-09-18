from django.urls import path
from .views import create, update, delete, read

from .views import TokenPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('token/', TokenPairView.as_view(), name='token'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('users/', read, name='userList'),
    path('users/create/', create, name='createUser'),

]