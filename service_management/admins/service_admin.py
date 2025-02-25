from django import forms
from django.contrib import admin
from service_management.models.service_model import ServiceModel
from service_management.models.service_product_model import ServiceProductModel

class ServiceCustomForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=ServiceProductModel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ServiceModel
        fields = '__all__'

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceCustomForm
    list_display = ['name', 'price', 'get_products', 'get_category', 'medspa']

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.get_products()])
    get_products.short_description = 'Products'

    def get_category(self, obj):
        return obj.get_category()
    get_category.short_description = 'Category'