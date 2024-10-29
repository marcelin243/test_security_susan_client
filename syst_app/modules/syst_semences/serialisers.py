from rest_framework import serializers
from syst_app.models import syst_semences

from syst_app.modules.syst_type_semences.serialisers import syst_type_semencesSerializers
from syst_app.modules.syst_categorie_semences.serialisers import syst_categorie_semencesSerializers

# SERIALIZERS  SYST SEMENCE
# =====================================
class syst_semencesSerializers(serializers.ModelSerializer):
    TYPE_SEMENCE_ID= syst_type_semencesSerializers()
    ID_CAT_SEMENCE=syst_categorie_semencesSerializers()
    
    
    class Meta:
        model=syst_semences
        fields="__all__"  
            
class insert_syst_semencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_semences
        fields="__all__"      