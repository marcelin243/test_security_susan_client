from rest_framework import serializers
from syst_app.models import syst_type_vehicule

class syst_type_vehiculeSerializers(serializers.ModelSerializer):

    class Meta:
        model=syst_type_vehicule
        fields="__all__"


      