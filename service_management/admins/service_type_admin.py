from django import forms
from django.contrib import admin
from service_management.models.service_product_model import ServiceProductModel
from service_management.models.service_type_model import ServiceTypeModel

@admin.register(ServiceTypeModel)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]