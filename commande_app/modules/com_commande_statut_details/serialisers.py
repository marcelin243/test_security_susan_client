from rest_framework import serializers
from commande_app.models import com_commande_statut_details

class insert_com_commande_statut_details_Serializers(serializers.ModelSerializer):
    class Meta:
        model=com_commande_statut_details
        fields="__all__"


      