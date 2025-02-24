from django.db import models
from suppliers.models import SupplierModel

class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Service Product"
        verbose_name_plural = "Services Products"

    def __str__(self):
        return self.name
