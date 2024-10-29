from rest_framework import serializers
from commande_app.models import com_paiement_commande
from commande_app.modules.com_commande.serialisers import *
from commande_app.modules.com_commande_detail.serialisers import *
from syst_app.modules.syst_mode_paiement.serialisers import *

class jointure_com_paiement_commande_Serializers(serializers.ModelSerializer):
    COMMANDE_ID=insert_com_commande_detail_Serializers()
    MODE_PAIEMENT_ID=insert_syst_mode_paiement_Serializers()
    
    class Meta:
        model=com_paiement_commande
        fields="__all__"    
          
class insert_com_paiement_commande_Serializers(serializers.ModelSerializer):
    class Meta:
        model=com_paiement_commande
        fields="__all__"      