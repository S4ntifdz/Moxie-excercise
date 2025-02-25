from django.db import models

from medspas.models import MedspaModel
from service_management.models.service_category_model import ServiceCategoryModel
from service_management.models.service_product_model import ServiceProductModel
from service_management.models.service_type_model import ServiceTypeModel

class ServiceModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True,)
    medspa = models.ForeignKey(MedspaModel, on_delete=models.CASCADE, related_name="services")
    product = models.ForeignKey(ServiceProductModel, on_delete=models.CASCADE, related_name='services')

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.name} - {self.product.service_type.name} ({self.medspa.name})"

    def get_products(self):
        return self.product.service_type.products.all()
    
    def get_category(self):
        return self.product.service_type.category.name