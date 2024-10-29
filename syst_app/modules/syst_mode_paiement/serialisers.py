from rest_framework import serializers
from syst_app.models import syst_mode_paiement

class insert_syst_mode_paiement_Serializers(serializers.ModelSerializer):

    class Meta:
        model=syst_mode_paiement
        fields="__all__" 


      