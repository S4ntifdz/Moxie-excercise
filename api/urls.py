from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views.appointment.appointment_view import AppointmentView
from api.views.medspas.medspa_view import MedspaView
from api.views.services.service_category_view import ServiceCategoryView
from api.views.services.service_products_view import ServiceProductView
from api.views.services.service_type_view import ServiceTypeView
from api.views.services.service_view import ServiceView
from api.views.suppliers.supplier_view import SupplierView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'medspas', MedspaView)
router.register(r'appointments', AppointmentView)
router.register(r'services', ServiceView)
router.register(r'service_types', ServiceTypeView)
router.register(r'service_categories', ServiceCategoryView)
router.register(r'products', ServiceProductView)
router.register(r'suppliers', SupplierView)

schema_view = get_schema_view(
    openapi.Info(
        title="Moxie API",
        default_version='v1',
        description="API documentation for Moxie project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
