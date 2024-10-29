from rest_framework import serializers
from syst_app.models import syst_categorie_semences

# SERIALIZERS  syst_categorie_semences
# =====================================
class syst_categorie_semencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_categorie_semences
        fields="__all__"      