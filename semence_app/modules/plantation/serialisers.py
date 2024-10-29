from rest_framework import serializers
from .models import plantation
from semence_app.modules.proprietaires.serialisers import proprietairesSerializers

from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers
# SERIALIZERS  plantation
# =====================================
class plantationSerializers(serializers.ModelSerializer):

    ID_PROPRIETAIRE=proprietairesSerializers()
    
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    
    class Meta:
        model=plantation
        fields="__all__"  
            
class insert_plantationSerializers(serializers.ModelSerializer):
    class Meta:
        model=plantation
        fields="__all__"      