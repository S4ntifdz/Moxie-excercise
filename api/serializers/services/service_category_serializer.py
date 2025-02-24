from rest_framework import serializers
from service_management.models.service_category_model import ServiceCategoryModel

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategoryModel
        fields = '__all__'