from rest_framework import serializers
from user_app.models import admin_profil

class admin_profilSerializers(serializers.ModelSerializer):

    class Meta:
        model=admin_profil
        fields="__all__"


      