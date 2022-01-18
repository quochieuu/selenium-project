from rest_framework import serializers
from .models import Data
class CreateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'name', 'address', 'acreage', 'link', 'price', 'description']