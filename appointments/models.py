import uuid
from django.db import models
from service_management.models.service_model import ServiceModel
from medspas.models import MedspaModel

class AppointmentStatus(models.TextChoices):
    SCHEDULED = 'Scheduled'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'

class AppointmentModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(blank=False, null=False)
    total_duration = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    medspa = models.ForeignKey(MedspaModel, on_delete=models.CASCADE)
    services = models.ManyToManyField(ServiceModel)
    status = models.CharField(max_length=10, choices=AppointmentStatus.choices, default=AppointmentStatus.SCHEDULED)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return f"Appointment {self.uuid}"

    def get_total_duration(self):
        return sum(service.duration for service in self.services.all())

    def get_total_price(self):
        return sum(service.price for service in self.services.all())