from rest_framework import viewsets
from api.serializers.suppliers.supplier_serializer import SupplierSerializer
from config.models import ConfigModel
from suppliers.models import SupplierModel
from rest_framework.permissions import IsAuthenticated

class SupplierView(viewsets.ModelViewSet):
    queryset = SupplierModel.objects.all()
    serializer_class = SupplierSerializer

    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(SupplierView, self).get_permissions()