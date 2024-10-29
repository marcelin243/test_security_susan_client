from rest_framework import serializers
from .models import proprietaires
from semence_app.modules.type_proprietaire.serialisers import type_proprietaireSerializers
from semence_app.modules.categorie_personne_morale.serialisers import categorie_personne_moraleSerializers
from semence_app.modules.type_document.serialisers import type_documentSerializers

from syst_app.modules.syst_provinces.serialisers import syst_provincesSerializers
from syst_app.modules.syst_collines.serialisers import syst_collinesSerializers
from syst_app.modules.syst_communes.serialisers import syst_communesSerializers
from syst_app.modules.syst_zones.serialisers import syst_zonesSerializers
# SERIALIZERS  proprietaires
# =====================================
class proprietairesSerializers(serializers.ModelSerializer):
    TYPE_PROPRIETAIRE_ID=type_proprietaireSerializers()
    ID_TYPE_DOCUMENT=type_documentSerializers()
    CATEGORIE_ID=categorie_personne_moraleSerializers()
    
    PROVINCE_ID=syst_provincesSerializers()
    COMMUNE_ID=syst_communesSerializers()
    ZONE_ID=syst_zonesSerializers()
    COLLINE_ID=syst_collinesSerializers()
    
    class Meta:
        model=proprietaires
        fields="__all__"  
            
class insert_proprietairesSerializers(serializers.ModelSerializer):
    class Meta:
        model=proprietaires
        fields="__all__"      