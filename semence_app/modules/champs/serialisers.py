from rest_framework import serializers
from .models import champs

from semence_app.modules.plantation.serialisers import plantationSerializers
from user_app.modules.admin_user.serialisers import joint_admin_userSerializers
from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers
# SERIALIZERS  champs
# =====================================
class champsSerializers(serializers.ModelSerializer):

    USER_ID=joint_admin_userSerializers()
    ID_PLANTATION=plantationSerializers()
    
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    
    class Meta:
        model=champs
        fields="__all__"  
            
class insert_champsSerializers(serializers.ModelSerializer):
    class Meta:
        model=champs
        fields="__all__"      