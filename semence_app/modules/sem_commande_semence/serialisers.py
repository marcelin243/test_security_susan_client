from rest_framework import serializers
from .models import sem_commande_semence
from semence_app.modules.proprietaires.serialisers import proprietairesSerializers
from semence_app.modules.sem_commande_semences_statut.serialisers import sem_commande_semences_statutSerializers

# SERIALIZERS  sem_commande_semence
# =====================================
class sem_commande_semenceSerializers(serializers.ModelSerializer):
    ID_PROPRIETAIRE=proprietairesSerializers()
    STATUT_CMD_ID=sem_commande_semences_statutSerializers()
    class Meta:
        model=sem_commande_semence
        fields="__all__"    
          
class insert_sem_commande_semenceSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_commande_semence
        fields="__all__"      