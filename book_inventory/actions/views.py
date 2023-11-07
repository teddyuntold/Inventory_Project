from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Actions
from .serializers import ActionSerializer

class CreateActionView(generics.ListCreateAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer

class UpdateDeleteActionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer
