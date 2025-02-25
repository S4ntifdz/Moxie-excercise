from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from appointments.models import AppointmentModel
from appointments.services.appointment_service import unique_appointment

def calculate_totals(instance):
    instance.total_duration = instance.get_total_duration()
    instance.total_price = instance.get_total_price()

@receiver(m2m_changed, sender=AppointmentModel.services.through)
def update_totals(sender, instance, **kwargs):
    calculate_totals(instance)
    instance.save()

@receiver(pre_save, sender=AppointmentModel)
def set_totals(sender, instance, **kwargs):
    calculate_totals(instance)
    unique_appointment(instance)