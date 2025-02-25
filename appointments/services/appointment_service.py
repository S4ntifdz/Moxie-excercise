from django.core.exceptions import ValidationError

def unique_appointment(appointment):
    from appointments.models import AppointmentModel
    overlapping_appointments = AppointmentModel.objects.filter(
        medspa=appointment.medspa,
        start_time__lt=appointment.end_time,
        end_time__gt=appointment.start_time,
        services__in=appointment.services.all()
    ).exclude(pk=appointment.pk).distinct()


    if overlapping_appointments.exists():
        raise ValidationError("This appointment overlaps with another appointment in the same medspa")
    else:
        return True