from django.db import models
from service_management.models.service_type_model import ServiceTypeModel
from suppliers.models import SupplierModel


class ServiceProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE, null=True, blank=True)
    service_type = models.ForeignKey(ServiceTypeModel, on_delete=models.CASCADE, related_name="services")

    class Meta:
        verbose_name = "Service Product"
        verbose_name_plural = "Services Products"

    def __str__(self):
        return self.name
