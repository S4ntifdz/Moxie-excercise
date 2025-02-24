from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.appointment.appointment_view import AppointmentView
from api.views.medspas.medspa_view import MedspaView
from api.views.products.product_view import ProductView
from api.views.services.service_category_view import ServiceCategoryView
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
router.register(r'products', ProductView)
router.register(r'suppliers', SupplierView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
