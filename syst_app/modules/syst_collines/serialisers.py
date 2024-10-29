from rest_framework import serializers
from syst_app.models import syst_collines
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers

# SERIALIZERS  syst_collines
# =====================================
class syst_collinesSerializers(serializers.ModelSerializer):
    ZONE_ID=syst_zonesSerializers()
    class Meta:
        model=syst_collines
        fields="__all__"      