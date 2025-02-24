from rest_framework import serializers
from api.serializers.services.service_serializer import ServiceSerializer
from appointments.models import AppointmentModel

class AppointmentSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only = True)
    class Meta:
        model = AppointmentModel
        fields = '__all__'