from django import forms
from django.contrib import admin
from appointments.models import AppointmentModel
from service_management.models.service_model import ServiceModel
from medspas.models import MedspaModel

class AppointmentCustomForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=ServiceModel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = AppointmentModel
        fields = '__all__'
        exclude = {
            'total_duration',
            'total_price',
            'end_time',
        }

@admin.register(AppointmentModel)
class AppointmentsAdmin(admin.ModelAdmin):
    form = AppointmentCustomForm
    list_display = ('medspa', 'total_price', 'total_duration','start_time','end_time','medspa')

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_services.short_description = 'Services'