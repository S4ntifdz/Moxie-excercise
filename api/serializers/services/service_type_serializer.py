from rest_framework import serializers
from api.serializers.services.service_product_serializer import ServiceProductSerializer
from service_management.models.service_type_model import ServiceTypeModel

class ServiceTypeSerializer(serializers.ModelSerializer):
    products = ServiceProductSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceTypeModel
        fields = '__all__'