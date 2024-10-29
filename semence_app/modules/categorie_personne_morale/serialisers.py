from rest_framework import serializers
from .models import categorie_personne_morale

# SERIALIZERS  categorie_personne_morale
# =====================================
class categorie_personne_moraleSerializers(serializers.ModelSerializer):
    class Meta:
        model=categorie_personne_morale
        fields="__all__"      