from rest_framework import viewsets
from api.serializers.services.service_category_serializer import ServiceCategorySerializer
from service_management.models.service_category_model import ServiceCategoryModel
from rest_framework.permissions import IsAuthenticated


class ServiceCategoryView(viewsets.ModelViewSet):
    queryset = ServiceCategoryModel.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticated]