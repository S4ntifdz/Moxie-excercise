from rest_framework import viewsets
from config.models import ConfigModel
from medspas.models import MedspaModel
from api.serializers.medspas.medspa_serializer import MedspaSerializer
from rest_framework.permissions import IsAuthenticated

class MedspaView(viewsets.ModelViewSet):
    queryset = MedspaModel.objects.all()
    serializer_class = MedspaSerializer
    
    def get_permissions(self):
        config = ConfigModel.objects.first()
        if config and config.enable_auth_token:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super(MedspaView, self).get_permissions()