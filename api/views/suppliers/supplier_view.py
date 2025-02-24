from rest_framework import viewsets
from api.serializers.suppliers.supplier_serializer import SupplierSerializer
from suppliers.models import SupplierModel

class SupplierView(viewsets.ModelViewSet):
    queryset = SupplierModel.objects.all()
    serializer_class = SupplierSerializer