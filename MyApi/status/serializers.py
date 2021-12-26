from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import Status #importing model

class StatusSerializer(serializers.ModelSerializer):
      class Meta:
            model= Status # which model data it will serialize
            fields= ['id','user','content','image'] # which fields will be serialized