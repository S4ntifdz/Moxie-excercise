import uuid
from django.db import models


class MedspaModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=256, null=False, blank=False)
    email_address = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
            verbose_name = "Medspa"
            verbose_name_plural = "Medspas"

    def __str__(self):
        return self.name