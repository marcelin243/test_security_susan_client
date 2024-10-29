from rest_framework import serializers
from syst_app.models import syst_unite_mesure

class syst_unite_mesureSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_unite_mesure
        fields="__all__"
        
class customsyst_unite_mesureSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_unite_mesure
        fields=["UNITE_MESURE_ID","UNITE_MESURE_DESCR"]


      