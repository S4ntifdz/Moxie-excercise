from django import forms
from django.contrib import admin
from service_management.models.service_product_model import ServiceProductModel
from service_management.models.service_type_model import ServiceTypeModel

class ServiceTypeCustomForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=ServiceProductModel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ServiceProductModel
        fields = '__all__'

@admin.register(ServiceTypeModel)
class ServiceTypeAdmin(admin.ModelAdmin):
    form = ServiceTypeCustomForm
    list_display = ['name',]