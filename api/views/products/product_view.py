from rest_framework import viewsets
from api.serializers.products.product_serializer import ProductSerializer
from products.models import ProductModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [IsAuthenticated]