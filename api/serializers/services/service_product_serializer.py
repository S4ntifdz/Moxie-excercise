from rest_framework import serializers
from api.serializers.suppliers.supplier_serializer import SupplierSerializer
from service_management.models.service_product_model import ServiceProductModel

class ServiceProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer( read_only=True)
    class Meta:
        model = ServiceProductModel
        fields = '__all__'