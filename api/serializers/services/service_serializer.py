from rest_framework import serializers
from service_management.models.service_model import ServiceModel

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'