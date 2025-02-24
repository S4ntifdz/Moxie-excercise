from django import forms
from django.contrib import admin
from products.models import ProductModel
from service_management.models.service_type_model import ServiceTypeModel

class ServiceTypeCustomForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=ProductModel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ProductModel
        fields = '__all__'

@admin.register(ServiceTypeModel)
class ServiceTypeAdmin(admin.ModelAdmin):
    form = ServiceTypeCustomForm
    list_display = ['name',]