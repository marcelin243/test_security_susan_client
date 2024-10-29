from rest_framework import serializers
from syst_app.models import syst_filiere

class syst_filiereSerializers(serializers.ModelSerializer):

    class Meta:
        model=syst_filiere
        fields="__all__"


      