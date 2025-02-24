from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'

    def ready(self) -> None:
        from appointments.models import AppointmentModel
        from appointments.signals import pre_save_appointment_signal