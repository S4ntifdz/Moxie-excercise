from django.apps import AppConfig


class ServiceManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service_management'

    def ready(self) -> None:
        from service_management.admins import (
            service_admin,
            service_category_admin,
            service_type_admin,
            service_product_admin,
        )
        from service_management.models import (
            service_category_model,
            service_model,
        )