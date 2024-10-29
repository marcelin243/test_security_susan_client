from rest_framework import serializers
from user_app.models import acteur_infos
from user_app.modules.acteur_statut_juridique.serialisers import acteur_statut_juridiqueSerializers
from user_app.modules.admin_profil_user.serialisers import admin_profilSerializers
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers

# SERIALIZERS  acteur_infos
# =====================================
class acteur_infosSerializers(serializers.ModelSerializer):
    STATUT_JURIDIQUE_ID=acteur_statut_juridiqueSerializers()
    PROFIL_ID=admin_profilSerializers()
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    class Meta:
        model=acteur_infos
        fields="__all__"    
          
class insert_acteur_infosSerializers(serializers.ModelSerializer):
    class Meta:
        model=acteur_infos
        fields="__all__"   
        
        
    