from rest_framework import serializers
from syst_app.models import syst_zones
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers

# SERIALIZERS  syst_zones
# =====================================
class syst_zonesSerializers(serializers.ModelSerializer):
    COMMUNE_ID=syst_communesSerializers()
    class Meta:
        model=syst_zones
        fields="__all__"      