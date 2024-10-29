from rest_framework import serializers
from .models import ch_variete
from semence_app.modules.filieres.serialisers import filieresSerializers

# SERIALIZERS  ch_variete
# =====================================
class ch_varieteSerializers(serializers.ModelSerializer):
    ID_FILIERE=filieresSerializers()
    class Meta:
        model=ch_variete
        fields="__all__"    
          
class insert_ch_varieteSerializers(serializers.ModelSerializer):
    class Meta:
        model=ch_variete
        fields="__all__"      