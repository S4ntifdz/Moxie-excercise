from rest_framework import viewsets
from api.serializers.services.service_type_serializer import ServiceTypeSerializer
from config.models import ConfigModel
from service_management.models.service_type_model import ServiceTypeModel
from rest_framework.permissions import IsAuthenticated


class ServiceTypeView(viewsets.ModelViewSet):
    queryset = ServiceTypeModel.objects.all()
    serializer_class = ServiceTypeSerializer

    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(ServiceTypeView, self).get_permissions()