from rest_framework import viewsets
from api.serializers.services.service_category_serializer import ServiceCategorySerializer
from config.models import ConfigModel
from service_management.models.service_category_model import ServiceCategoryModel
from rest_framework.permissions import IsAuthenticated


class ServiceCategoryView(viewsets.ModelViewSet):
    queryset = ServiceCategoryModel.objects.all()
    serializer_class = ServiceCategorySerializer
    
    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(ServiceCategoryView, self).get_permissions()