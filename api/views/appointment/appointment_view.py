from rest_framework import viewsets
from api.serializers.appointments.appointment_serializer import AppointmentSerializer
from appointments.models import AppointmentModel
from rest_framework.permissions import IsAuthenticated


class AppointmentView(viewsets.ModelViewSet):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]