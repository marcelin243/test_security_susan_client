from rest_framework import serializers
from syst_app.models import syst_communes
from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers

# SERIALIZERS  syst_communes
# =====================================
class syst_communesSerializers(serializers.ModelSerializer):
    PROVINCE_ID=syst_provincesSerializers()
    class Meta:
        model=syst_communes
        fields="__all__"      