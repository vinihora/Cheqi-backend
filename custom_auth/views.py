from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = [AllowAny]
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]