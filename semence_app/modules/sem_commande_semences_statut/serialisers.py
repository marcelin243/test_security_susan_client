from rest_framework import serializers
from .models import sem_commande_semences_statut

# SERIALIZERS  sem_commande_semences_statut
# =====================================
class sem_commande_semences_statutSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_commande_semences_statut
        fields="__all__"      