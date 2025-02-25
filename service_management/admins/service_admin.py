from django.contrib import admin
from service_management.models.service_model import ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'get_products', 'get_category', 'medspa']

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.product.service_type.products.all()])
    get_products.short_description = 'Products'

    def get_category(self, obj):
        return obj.get_category()
    get_category.short_description = 'Category'