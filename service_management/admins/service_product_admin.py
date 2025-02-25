from django.contrib import admin
from service_management.models.service_product_model import ServiceProductModel
from service_management.models.service_model import ServiceModel

@admin.register(ServiceProductModel)
class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ['name',]