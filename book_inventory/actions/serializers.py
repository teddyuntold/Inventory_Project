from rest_framework import serializers
from .models import Actions

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'
