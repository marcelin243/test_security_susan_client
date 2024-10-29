from django.db import models

# *****************************************************************************************
# MODEL SYST TYPE VEHICULE
# *****************************************************************************************
class syst_type_vehicule(models.Model):
    TYPE_VEHICULE_ID=models.BigAutoField(primary_key=True,db_column='TYPE_VEHICULE_ID') 
    TYPE_VEHICULE_DESC=models.CharField(max_length=50,null=True,db_column='TYPE_VEHICULE_DESC')
    class Meta:
        db_table = 'syst_type_vehicule'
        
    def __str__(self):
        return self.TYPE_VEHICULE_DESC
    
# ***************************************************************************************************
# MODEL PRONVINCE
# **************************************************************************************************
class syst_provinces(models.Model):
    PROVINCE_ID=models.AutoField(primary_key=True,db_column='PROVINCE_ID')
    OBJECTIF=models.IntegerField(null=True,db_column="OBJECTIF")
    IS_ACTIVE=models.SmallIntegerField(null=True,db_column="IS_ACTIVE")
    PROVINCE_NAME=models.CharField(max_length=255,null=False,db_column="PROVINCE_NAME")
    PROVINCE_LATITUDE=models.CharField(max_length=255,null=False,db_column="PROVINCE_LATITUDE")
    PROVINCE_LONGITUDE=models.CharField(max_length=255,null=False,db_column="PROVINCE_LONGITUDE")
    POLY=models.TextField(null=False,db_column="POLY")
    
    class Meta:
        db_table = 'syst_provinces'
         
    def __str__(self):
        return self.PROVINCE_NAME
    
# *********************************************************************************************
# MODEL COMMUNE
# *******************************************************************************************
class syst_communes(models.Model):
    COMMUNE_ID=models.AutoField(primary_key=True,db_column='COMMUNE_ID')
    COMMUNE_NAME=models.CharField(max_length=255,null=False,db_column="COMMUNE_NAME")
    COMMUNE_LATITUDE=models.CharField(max_length=255,null=False,db_column="COMMUNE_LATITUDE")
    COMMUNE_LONGITUDE=models.CharField(max_length=255,null=False,db_column="COMMUNE_LONGITUDE")
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    
    class Meta:
        db_table = 'syst_communes'
         
    def __str__(self):
        return self.COMMUNE_NAME
    
# **********************************************************************************************
# MODEL ZONE
# ***************************************************************************************************
class syst_zones(models.Model):
    ZONE_ID=models.AutoField(primary_key=True,db_column='ZONE_ID')
    ZONE_NAME=models.CharField(max_length=255,null=False,db_column="ZONE_NAME")
    LATITUDE=models.CharField(max_length=255,null=False,db_column="LATITUDE")
    LONGITUDE=models.CharField(max_length=255,null=False,db_column="LONGITUDE")
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    
    class Meta:
        db_table = 'syst_zones'
         
    def __str__(self):
        return self.ZONE_NAME
    
# *****************************************************************************************
# MODEL COLLINE
# *************************************************************************
class syst_collines(models.Model):
    COLLINE_ID=models.AutoField(primary_key=True,db_column='COLLINE_ID')
    COLLINE_NAME=models.CharField(max_length=255,null=False,db_column="COLLINE_NAME")
    LATITUDE=models.CharField(max_length=255,null=False,db_column="LATITUDE")
    LONGITUDE=models.CharField(max_length=255,null=False,db_column="LONGITUDE")
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    
    class Meta:
        db_table = 'syst_collines'
         
    def __str__(self):
        return self.COLLINE_NAME
    
# *****************************************************************************************
# MODEL CATEGORIE SEMENCE
# *************************************************************************
class syst_categorie_semences(models.Model):
    ID_CAT_SEMENCE =models.AutoField(primary_key=True,db_column='ID_CAT_SEMENCE')
    CAT_SEMENCES=models.CharField(max_length=255,null=False,db_column="CAT_SEMENCES")
    
    class Meta:
        db_table = 'syst_categorie_semences'
         
    def __str__(self):
        return self.CAT_SEMENCES
    
# *****************************************************************************************
# MODEL TYPE SEMENCE
# *************************************************************************
class syst_type_semences(models.Model):
    TYPE_SEMENCE_ID =models.AutoField(primary_key=True,db_column='TYPE_SEMENCE_ID')
    TYPE_SEMENCE_DESC=models.CharField(max_length=255,null=False,db_column="TYPE_SEMENCE_DESC")
    
    class Meta:
        db_table = 'syst_type_semences'
         
    def __str__(self):
        return self.TYPE_SEMENCE_DESC
# *****************************************************************************************
# MODEL COLLINE
# *************************************************************************
class syst_semences(models.Model):
    SEMENCE_ID=models.AutoField(primary_key=True,db_column='SEMENCE_ID')
    SEMENCE_DESCR=models.CharField(max_length=100,null=True,db_column="SEMENCE_DESCR")
    TYPE_SEMENCE_ID=models.ForeignKey(syst_type_semences,on_delete=models.CASCADE,db_column='TYPE_SEMENCE_ID')
    ID_CAT_SEMENCE=models.ForeignKey(syst_categorie_semences,on_delete=models.CASCADE,db_column='ID_CAT_SEMENCE')
    
    
    class Meta:
        db_table = 'syst_semences'
         
    def __str__(self):
        return self.SEMENCE_DESCR
# *****************************************************************************************
# MODEL FILIERE
# *************************************************************************

class syst_filiere(models.Model):
    ID_FILIERE=models.AutoField(primary_key=True,db_column='ID_FILIERE')
    NOM_FILIERE=models.CharField(max_length=50,null=False,db_column="NOM_FILIERE")
    CODE_COULEUR=models.CharField(max_length=20,null=True,db_column="CODE_COULEUR")
    IMAGE=models.ImageField(max_length=255,upload_to="syst_filiere/image",null=True,db_column="IMAGE")
    FICHE_TECHNIQUE=models.FileField(max_length=255,upload_to="syst_filiere/FICHE_TECHNIQUE",null=True,db_column="FICHE_TECHNIQUE")
    VALEUR_NORMALE_HS=models.FloatField(null=True,db_column="VALEUR_NORMALE_HS")
    VALEUR_NORMALE_TEMPERATURE=models.FloatField(null=True,db_column="VALEUR_NORMALE_TEMPERATURE")
    
    class Meta:
        db_table = 'syst_filiere'
         
    def __str__(self):
        return self.NOM_FILIERE
    
# *****************************************************************************************
# MODEL UNITE DE MESURE
# *************************************************************************

class syst_unite_mesure(models.Model):
    UNITE_MESURE_ID=models.AutoField(primary_key=True,db_column='UNITE_MESURE_ID')
    UNITE_MESURE_DESCR=models.CharField(max_length=15,null=True,db_column="UNITE_MESURE_DESCR")
    UNITE_MESURE_SYMBOLE=models.CharField(max_length=5,null=True,db_column="UNITE_MESURE_SYMBOLE")
    class Meta:
        db_table = 'syst_unite_mesure'
         
    def __str__(self):
        return self.UNITE_MESURE_DESCR
    
# *****************************************************************************************
# MODEL MODE PAYEMENT
# *************************************************************************
class syst_mode_paiement(models.Model):
    MODE_PAIEMENT_ID=models.AutoField(primary_key=True,db_column='MODE_PAIEMENT_ID')
    MODE_PAIEMENT_DESCR=models.CharField(max_length=50,null=False,db_column="MODE_PAIEMENT_DESCR")
    
    class Meta:
        db_table = 'syst_mode_paiement'
         
    def __str__(self):
        return self.MODE_PAIEMENT_DESCR


