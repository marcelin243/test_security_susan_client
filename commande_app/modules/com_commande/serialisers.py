from rest_framework import serializers
from commande_app.models import com_commande
from commande_app.modules.com_commande_statut.serialisers import insert_com_commande_statut_Serializers
class jointure_com_commande_Serializers(serializers.ModelSerializer):
    STATUT_COM_ID=insert_com_commande_statut_Serializers()
    
    class Meta:
        model=com_commande
        fields="__all__"
class insert_com_commande_Serializers(serializers.ModelSerializer):

    class Meta:
        model=com_commande
        fields="__all__"
        


      