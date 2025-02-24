from rest_framework import serializers
from medspas.models import MedspaModel

class MedspaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedspaModel
        fields = '__all__'