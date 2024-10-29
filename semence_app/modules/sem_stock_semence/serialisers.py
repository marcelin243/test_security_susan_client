from rest_framework import serializers
from .models import sem_stock_semence
from semence_app.modules.filieres.serialisers import filieresSerializers

from semence_app.modules.ch_variete.serialisers import ch_varieteSerializers
from semence_app.modules.proprietaires.serialisers import proprietairesSerializers
from semence_app.modules.type_semences.serialisers import type_semencesSerializers

# SERIALIZERS  sem_stock_semence
# =====================================
class sem_stock_semenceSerializers(serializers.ModelSerializer):
    FILIERE_ID=filieresSerializers()
    VARIETE_ID=ch_varieteSerializers()
    ID_PROPRIETAIRE=proprietairesSerializers()
    ID_TYPE_SEMENCES=type_semencesSerializers()
    class Meta:
        model=sem_stock_semence
        fields="__all__"    
          
class insert_sem_stock_semenceSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_stock_semence
        fields="__all__"      