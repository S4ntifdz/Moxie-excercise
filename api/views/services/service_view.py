from rest_framework import viewsets
from api.serializers.services.service_serializer import ServiceSerializer
from config.models import ConfigModel
from service_management.models.service_model import ServiceModel
from rest_framework.permissions import IsAuthenticated


class ServiceView(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(ServiceView, self).get_permissions()