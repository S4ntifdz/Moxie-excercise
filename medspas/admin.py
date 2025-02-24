from django.contrib import admin

from medspas.models import MedspaModel


@admin.register(MedspaModel)
class MedspaAdmin(admin.ModelAdmin):
    list_display = ['name',]