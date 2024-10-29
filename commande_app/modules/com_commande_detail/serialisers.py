from rest_framework import serializers
from commande_app.models import com_commande_detail
from commande_app.modules.com_commande_statut_details.serialisers import *

class jointure_com_commande_detail_Serializers(serializers.ModelSerializer):
    COM_STATUT_DET_ID=insert_com_commande_statut_details_Serializers()
    class Meta:
        model=com_commande_detail
        fields="__all__"    
          
class insert_com_commande_detail_Serializers(serializers.ModelSerializer):
    class Meta:
        model=com_commande_detail
        fields="__all__"      