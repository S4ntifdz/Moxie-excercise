from rest_framework import serializers
from api.serializers.suppliers.supplier_serializer import SupplierSerializer
from products.models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer( read_only=True)
    class Meta:
        model = ProductModel
        fields = '__all__'