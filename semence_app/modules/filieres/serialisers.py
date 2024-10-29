from rest_framework import serializers
from .models import filieres

# SERIALIZERS  filieres
# =====================================
class filieresSerializers(serializers.ModelSerializer):
    class Meta:
        model=filieres
        fields="__all__"      