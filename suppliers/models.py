from django.db import models

class SupplierModel(models.Model):
    name = models.CharField(max_length=256)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
            verbose_name = "Supplier"
            verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name