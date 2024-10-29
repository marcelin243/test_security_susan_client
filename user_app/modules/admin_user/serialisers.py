from rest_framework import serializers
from user_app.models import admin_user
from user_app.modules.admin_profil_user.serialisers import admin_profilSerializers
from user_app.modules.acteur_infos.serialisers import insert_acteur_infosSerializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class joint_admin_userSerializers(serializers.ModelSerializer):
    profil_id=admin_profilSerializers()
    acteur_id=insert_acteur_infosSerializers()
    class Meta:
        model=admin_user
        exclude = ['password']        
class insert_admin_userSerializers(serializers.ModelSerializer): 
    class Meta:
        model=admin_user
        fields="__all__"
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Ajouter des informations supplémentaires au payload du token
        token['email'] = user.email
        token['telephone'] = user.telephone
        token['nom'] = user.acteur_id.NOM
        token['prenom'] = user.acteur_id.PRENOM
        token['profil_descr'] = user.acteur_id.PROFIL_ID.profil_descr

        return token
        
