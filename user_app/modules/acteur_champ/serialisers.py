from rest_framework import serializers
from user_app.models import acteur_champ
from user_app.modules.acteur_statut_juridique.serialisers import acteur_statut_juridiqueSerializers
from user_app.modules.admin_profil_user.serialisers import admin_profilSerializers
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers
from semence_app.modules.filieres.serialisers import filieresSerializers
from user_app.modules.acteur_infos.serialisers import insert_acteur_infosSerializers
# SERIALIZERS  acteur_champ
# =====================================
class acteur_champSerializers(serializers.ModelSerializer):
    ID_FILIERE=filieresSerializers()
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    ACTEUR_ID=insert_acteur_infosSerializers()
    class Meta:
        model=acteur_champ
        fields="__all__"    
          
class insert_acteur_champSerializers(serializers.ModelSerializer):
    class Meta:
        model=acteur_champ
        fields="__all__"   
        
        
    