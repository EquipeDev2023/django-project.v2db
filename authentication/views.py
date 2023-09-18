from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from .serialize import srl_User

from assets.crud import crud
from datetime import datetime

class TokenPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

# Create your views here.
prepare = crud(request=None, model=User, srl_model=srl_User, key=None)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
    return prepare.read()

@api_view(['POST'])
def create(request):
    default_data = request.data

    default_data['password'] = make_password(default_data['password'])
    default_data['last_login'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    default_data['is_superuser'] = False
    default_data['is_staff'] = False
    default_data['is_active'] = True
    default_data['date_joined'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    default_data['groups'] = []
    default_data['user_permissions']=[]

    prepare.r = default_data
    return prepare.create()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update(request):
    return render(request, '')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request):
    return render(request, '')