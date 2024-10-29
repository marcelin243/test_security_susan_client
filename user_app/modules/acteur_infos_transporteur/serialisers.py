from rest_framework import serializers
from user_app.models import acteur_infos_transporteur
from syst_app.modules.syst_type_vehicule.serialisers import syst_type_vehiculeSerializers
from user_app.modules.acteur_infos.serialisers import insert_acteur_infosSerializers

class joint_acteur_infos_transporteurSerializers(serializers.ModelSerializer):
    TYPE_VEHICULE_ID=syst_type_vehiculeSerializers()
    ACTEUR_ID=insert_acteur_infosSerializers()
    class Meta:
        model=acteur_infos_transporteur
        fields="__all__"   
        
class insert_acteur_infos_transporteurSerializers(serializers.ModelSerializer): 
    class Meta:
        model=acteur_infos_transporteur
        fields="__all__"   