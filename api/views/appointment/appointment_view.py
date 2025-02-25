from rest_framework import viewsets
from api.serializers.appointments.appointment_serializer import AppointmentSerializer
from appointments.models import AppointmentModel
from rest_framework.permissions import IsAuthenticated

from config.models import ConfigModel


class AppointmentView(viewsets.ModelViewSet):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(AppointmentView, self).get_permissions()