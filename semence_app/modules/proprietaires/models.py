from django.db import models
from semence_app.modules.type_proprietaire.models import type_proprietaire
from semence_app.modules.categorie_personne_morale.models import categorie_personne_morale
from semence_app.modules.type_document.models import type_document
from syst_app.models import *



# MODEL proprietaires
# ==========================
class proprietaires(models.Model):
    ID_PROPRIETAIRE=models.AutoField(primary_key=True,db_column='ID_PROPRIETAIRE')
    TYPE_PROPRIETAIRE_ID=models.ForeignKey(type_proprietaire, null=True,on_delete=models.CASCADE,db_column='TYPE_PROPRIETAIRE_ID')
    # DESCR_SEMENCES=models.CharField(max_length=255,null=True,db_column="DESCR_SEMENCES")
    NOM_PROPRIETAIRE=models.CharField(max_length=50,null=True,db_column="NOM_PROPRIETAIRE")
    PRENOM_PROPRIETAIRE=models.CharField(max_length=50,null=True,db_column="PRENOM_PROPRIETAIRE")
    EMAIL_PROPRIETAIRE=models.CharField(max_length=25,null=True,db_column="EMAIL_PROPRIETAIRE")
    TEL_PROPRIETAIRE=models.CharField(max_length=15,null=True,db_column="TEL_PROPRIETAIRE")
    DATE_NAISSANCE=models.DateField(null=True,db_column="DATE_NAISSANCE")
    SITE_WEB=models.CharField(max_length=30,null=True,db_column="SITE_WEB")
    LIEU_NAISSANCE=models.CharField(max_length=50,null=True,db_column="LIEU_NAISSANCE")
    
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=True,on_delete=models.CASCADE,db_column='COLLINE_ID')
    
    ID_TYPE_DOCUMENT=models.ForeignKey(type_document, null=True,on_delete=models.CASCADE,db_column='ID_TYPE_DOCUMENT')
    CATEGORIE_ID=models.ForeignKey(categorie_personne_morale, null=True,on_delete=models.CASCADE,db_column='CATEGORIE_ID')
    NUMERO_WHATSAPP=models.CharField(max_length=25,null=True,db_column="NUMERO_WHATSAPP")
    REGISTRE_COMMERCE=models.CharField(max_length=25,null=True,db_column="REGISTRE_COMMERCE")
    NUMERO_DOCUMENT=models.CharField(max_length=15,null=True,db_column="NUMERO_DOCUMENT")
    TELEPHONE_FIXE=models.CharField(max_length=30,null=True,db_column="TELEPHONE_FIXE")
    ADRES_EMAIL=models.CharField(max_length=30,null=True,db_column="ADRES_EMAIL")
    NOMINATION=models.CharField(max_length=30,null=True,db_column="NOMINATION")
    NIF=models.CharField(max_length=25,null=True,db_column="NIF")
    STATUT=models.IntegerField(null=True,db_column="STATUT")
    SEXE_PROPRIETAIRE=models.SmallIntegerField(null=True,db_column="SEXE_PROPRIETAIRE")
    PHATH_PHOTO=models.FileField(upload_to="proprietaires/files/",null=True,db_column="PHATH_PHOTO")
    PATH_DOCUMENT=models.FileField(upload_to="proprietaires/files/",null=True,db_column="PATH_DOCUMENT")
    DATE_ENREGISTREMENT=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_ENREGISTREMENT")
    
    
    class Meta:
        db_table = 'proprietaires'
         
    def __str__(self):
        return self.NOM_PROPRIETAIRE