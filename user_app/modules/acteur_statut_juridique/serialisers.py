from rest_framework import serializers
from user_app.models import acteur_statut_juridique

class acteur_statut_juridiqueSerializers(serializers.ModelSerializer):

    class Meta:
        model=acteur_statut_juridique
        fields="__all__"


      