from rest_framework import serializers
from .models import sem_certification_activite

# SERIALIZERS  sem_certification_activite
# =====================================
class sem_certification_activiteSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_certification_activite
        fields="__all__"      