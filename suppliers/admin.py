from django.contrib import admin
from suppliers.models import SupplierModel

@admin.register(SupplierModel)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name',]