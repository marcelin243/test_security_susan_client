from rest_framework import serializers
from .models import type_proprietaire

# SERIALIZERS  type_proprietaire
# =====================================
class type_proprietaireSerializers(serializers.ModelSerializer):
    class Meta:
        model=type_proprietaire
        fields="__all__"      