<<<<<<< HEAD
from rest_framework import serializers
from .models import Actions

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'
=======
from rest_framework import serializers
from .models import Actions

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'
>>>>>>> 59d377753d1f1b0d186c349bc7c3a802a07a04c2
