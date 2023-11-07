<<<<<<< HEAD
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
=======
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
>>>>>>> 59d377753d1f1b0d186c349bc7c3a802a07a04c2
