from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from appointments.models import AppointmentModel

@receiver(m2m_changed, sender=AppointmentModel.services.through)
def update_totals(sender, instance, **kwargs):
    instance.total_duration = instance.get_total_duration()
    instance.total_price = instance.get_total_price()
    instance.save()

@receiver(pre_save, sender=AppointmentModel)
def set_totals(sender, instance, **kwargs):
    if not instance.pk:
        instance.total_duration = instance.get_total_duration()
        instance.total_price = instance.get_total_price()