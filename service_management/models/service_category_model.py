from django.db import models
from medspas.models import MedspaModel
from products.models import ProductModel

class ServiceCategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
