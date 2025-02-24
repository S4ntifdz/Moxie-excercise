from rest_framework import serializers
from service_management.models.service_type_model import ServiceTypeModel
from api.serializers.products.product_serializer import ProductSerializer

class ServiceTypeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceTypeModel
        fields = '__all__'