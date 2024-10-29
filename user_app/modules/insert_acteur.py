
from user_app.modules.acteur_infos.serialisers import insert_acteur_infosSerializers
from user_app.modules.acteur_champ.serialisers import insert_acteur_champSerializers
from user_app.modules.acteur_multi_semence.serialisers import insert_acteur_multi_semenceSerializers
from user_app.modules.acteur_infos_transporteur.serialisers import insert_acteur_infos_transporteurSerializers as info_trans
from user_app.modules.admin_user.serialisers import insert_admin_userSerializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

 
@api_view(['POST'])
def insert_acteur(request):
    # transporteur 8 , multiplicateur  6 , produicteur 2
    profil_user=request.data.get("PROFIL_ID")
    serialiser=insert_acteur_infosSerializers(data=request.data)
    serialiser.is_valid(raise_exception=True)
    serialiser.save()
    request.data["acteur_id"]=serialiser.instance.ACTEUR_ID

    request.data["password"]=make_password("12345678")
    request.data["profil_id"]=request.data.get("PROFIL_ID")
    request.data["telephone"]=request.data.get("TELEPHONE")
    request.data["email"]=request.data.get("EMAIL")
    
    serialiser_admin=insert_admin_userSerializers(data=request.data)
    serialiser_admin.is_valid(raise_exception=True)
    serialiser_admin.save()
    if profil_user==2:
        CHAMP=request.data.get("champs")
        for donn in CHAMP:
            
            data={
                "PROVINCE_ID":donn["PROVINCE_ID_CHAMP"],
                "COMMUNE_ID":donn["COMMUNE_ID_CHAMP"],
                "ZONE_ID":donn["ZONE_ID_CHAMP"],
                "COLLINE_ID":donn["COLLINE_ID_CHAMP"],
                "COORD_POLY":donn["COORD_POLY"],
                "CHAMP_DESC":donn["CHAMP_DESC"],
                "SUPERFICIE":donn["SUPERFICIE"],
                "ACTEUR_ID":serialiser.instance.ACTEUR_ID,
                "ID_FILIERE":donn["ID_FILIERE"],  
                }
            
            serialiser_champ=insert_acteur_champSerializers(data=data)
            serialiser_champ.is_valid(raise_exception=True)
            serialiser_champ.save()
        return Response({"detail":"save"})
 
    elif profil_user == 6:  # Profil multiplicateur
            CHAMP = request.data.get("champs")
            for donn in CHAMP:
                data = {
                    "PROVINCE_ID": donn["PROVINCE_ID_CHAMP"],  # Conversion en entier
                    "COMMUNE_ID": donn["COMMUNE_ID_CHAMP"],    # Conversion en entier
                    "ZONE_ID": donn["ZONE_ID_CHAMP"],          # Conversion en entier
                    "COLLINE_ID": donn["COLLINE_ID_CHAMP"],    # Conversion en entier
                    "CHAMP_DESC": donn["CHAMP_DESC"],
                    "SUPERFICIE": donn["SUPERFICIE"],        # Conversion en float
                    "ACTEUR_ID": serialiser.instance.ACTEUR_ID,
                    "ID_FILIERE": 10,
                }
                
                serialiser_champ = insert_acteur_champSerializers(data=data)
                serialiser_champ.is_valid(raise_exception=True)
                serialiser_champ.save()
            
            donnee = {
                "PROVINCE_ID": request.data.get("PROVINCE_ID_MULTI"),  # Conversion en entier
                "COMMUNE_ID": request.data.get("COMMUNE_ID_MULTI"),    # Conversion en entier
                "ZONE_ID": request.data.get("ZONE_ID_MULTI"),          # Conversion en entier
                "COLLINE_ID": request.data.get("COLLINE_ID_MULTI"),    # Conversion en entier
                "CAPACITE_MULTIPLICATION": request.data.get("CAPACITE_MULTIPLICATION"),  # Conversion en float
                "ACTEUR_ID": serialiser.instance.ACTEUR_ID,
                "UNITE_MESURE_ID": request.data.get("UNITE_MESURE_ID"),  # Conversion en entier
            }
            serialiser_multi = insert_acteur_multi_semenceSerializers(data=donnee)
            serialiser_multi.is_valid(raise_exception=True)
            serialiser_multi.save()
            return Response({"detail": "save"})
    
@api_view(['POST'])
def insert_transporteur(request):
    # transporteur 8 
    dann={
        "NOM":request.data.get("NOM"),
        "PRENOM":request.data.get("PRENOM"),
        "TELEPHONE":request.data.get("TELEPHONE"),
        "EMAIL":request.data.get("EMAIL"),
        "STATUT_JURIDIQUE_ID":int(request.data.get("STATUT_JURIDIQUE_ID")),
        "PROFIL_ID":int(request.data.get("PROFIL_ID")),
        "PROVINCE_ID":int(request.data.get("PROVINCE_ID")),
        "COMMUNE_ID":int(request.data.get("COMMUNE_ID")),
        "ZONE_ID":int(request.data.get("ZONE_ID")),
        "COLLINE_ID":int(request.data.get("COLLINE_ID")),
    }
    serialiser=insert_acteur_infosSerializers(data=dann)
    serialiser.is_valid(raise_exception=True)
    serialiser.save()
    mutable=request.data.copy()
    mutable["acteur_id"]=serialiser.instance.ACTEUR_ID
    mutable["password"]=make_password("12345678")
    mutable["profil_id"]=int(request.data.get("PROFIL_ID"))
    mutable["telephone"]=request.data.get("TELEPHONE")
    mutable["email"]=request.data.get("EMAIL")
    
    serialiser_admin=insert_admin_userSerializers(data=mutable)
    serialiser_admin.is_valid(raise_exception=True)
    serialiser_admin.save()
    
    mutable["ACTEUR_ID"]=serialiser.instance.ACTEUR_ID
    mutable["TYPE_VEHICULE_ID"]=int(request.data.get("TYPE_VEHICULE_ID"))
    mutable["LICENCE_TRANSPORT"]=request.FILES.get("LICENCE_TRANSPORT")
    serialiser_trans=info_trans(data=mutable)
    serialiser_trans.is_valid(raise_exception=True)
    serialiser_trans.save()
    return Response({"detail":"save"})