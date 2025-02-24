from rest_framework import viewsets
from medspas.models import MedspaModel
from api.serializers.medspas.medspa_serializer import MedspaSerializer
from rest_framework.permissions import IsAuthenticated

class MedspaView(viewsets.ModelViewSet):
    queryset = MedspaModel.objects.all()
    serializer_class = MedspaSerializer
    permission_classes = [IsAuthenticated]