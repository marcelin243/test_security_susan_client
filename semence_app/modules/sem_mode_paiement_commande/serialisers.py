from rest_framework import serializers
from .models import sem_mode_paiement_commande

# SERIALIZERS  sem_mode_paiement_commande
# =====================================
class sem_mode_paiement_commandeSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_mode_paiement_commande
        fields="__all__"      