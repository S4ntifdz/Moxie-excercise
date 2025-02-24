from django.contrib import admin
from service_management.models.service_category_model import ServiceCategoryModel
from service_management.models.service_model import ServiceModel

@admin.register(ServiceCategoryModel)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]