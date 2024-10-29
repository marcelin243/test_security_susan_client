from rest_framework import serializers
from user_app.models import acteur_multi_semence
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers
from syst_app.modules.syst_unite_mesure.serialisers import syst_unite_mesureSerializers
from user_app.modules.acteur_infos.serialisers import insert_acteur_infosSerializers
# SERIALIZERS  acteur_multi_semence
# =====================================
class acteur_multi_semenceSerializers(serializers.ModelSerializer):
   
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    ACTEUR_ID=insert_acteur_infosSerializers()
    UNITE_MESURE_ID=syst_unite_mesureSerializers()
    class Meta:
        model=acteur_multi_semence
        fields="__all__"    
          
class insert_acteur_multi_semenceSerializers(serializers.ModelSerializer):
    class Meta:
        model=acteur_multi_semence
        fields="__all__"   
        
        
    