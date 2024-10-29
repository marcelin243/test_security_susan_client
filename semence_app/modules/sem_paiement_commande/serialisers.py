from rest_framework import serializers
from .models import sem_paiement_commande
from semence_app.modules.filieres.serialisers import filieresSerializers

from semence_app.modules.sem_commande_semence.serialisers import sem_commande_semenceSerializers
from semence_app.modules.sem_mode_paiement_commande.serialisers import sem_mode_paiement_commandeSerializers

# SERIALIZERS  sem_paiement_commande
# =====================================
class sem_paiement_commandeSerializers(serializers.ModelSerializer):
    COMMANDE_ID=sem_commande_semenceSerializers()
    MODE_PAIEMENT_ID=sem_mode_paiement_commandeSerializers()

    class Meta:
        model=sem_paiement_commande
        fields="__all__"    
          
class insert_sem_paiement_commandeSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_paiement_commande
        fields="__all__"      