from django.db import models
from django.forms import ValidationError

class ConfigModel(models.Model):
    enable_auth_token = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def save(self, *args, **kwargs):
        if not self.pk and ConfigModel.objects.exists():
            raise ValidationError('There can be only one ConfigModel instance')
        return super(ConfigModel, self).save(*args, **kwargs)

    def __str__(self):
        return "Configuration"