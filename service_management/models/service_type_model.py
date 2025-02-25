from django.db import models
from service_management.models.service_category_model import ServiceCategoryModel


class ServiceTypeModel(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(ServiceCategoryModel, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "Service Type"
            verbose_name_plural = "Service Types"

    def __str__(self):
        return self.name
    
