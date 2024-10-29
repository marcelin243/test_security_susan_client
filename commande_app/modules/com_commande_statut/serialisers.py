from rest_framework import serializers
from commande_app.models import com_commande_statut

class insert_com_commande_statut_Serializers(serializers.ModelSerializer):

    class Meta:
        model=com_commande_statut
        fields="__all__"


      