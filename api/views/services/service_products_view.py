from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from api.serializers.services.service_product_serializer import ServiceProductSerializer
from config.models import ConfigModel
from service_management.models.service_product_model import ServiceProductModel

class ServiceProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ServiceProductView(viewsets.ModelViewSet):
    queryset = ServiceProductModel.objects.all().order_by('id')
    serializer_class = ServiceProductSerializer
    pagination_class = ServiceProductPagination

    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(ServiceProductView, self).get_permissions()