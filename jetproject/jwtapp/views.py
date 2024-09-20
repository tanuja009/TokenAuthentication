from django.shortcuts import render
from .serializers import mymodelserializer
from rest_framework import viewsets
from .models import mymodel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = mymodel.objects.all()
    serializer_class = mymodelserializer  # Specify the serializer class here
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

