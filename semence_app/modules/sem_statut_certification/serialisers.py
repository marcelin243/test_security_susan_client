from rest_framework import serializers
from .models import sem_statut_certification

# SERIALIZERS  sem_statut_certification
# =====================================
class sem_statut_certificationSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_statut_certification
        fields="__all__"      