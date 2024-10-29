from django.db import models
from syst_app.models import *       
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from autres_modules.manager import CustomUserManager

# *********************************************************************************************************
#                                   MODEL ACTEUR STATUT JUDICIERE
# *************************************************************************************************************
class acteur_statut_juridique(models.Model):
    STATUT_JURIDIQUE_ID =models.BigAutoField(primary_key=True,db_column='STATUT_JURIDIQUE_ID') 
    STATUT_JURIDIQUE_DESC=models.CharField(max_length=50,null=True,db_column='STATUT_JURIDIQUE_DESC')
    class Meta:
        db_table = 'acteur_statut_juridique'
        
    def __str__(self):
        return self.STATUT_JURIDIQUE_DESC 
    
# ***************************************************************************************************************
#                                                MODEL ADMIN PROFIL
# *************************************************************************************************************
class admin_profil(models.Model):
    profil_id=models.BigAutoField(primary_key=True,db_column='profil_id') 
    profil_descr=models.CharField(max_length=50,null=True,db_column='profil_descr')
    profil_code=models.CharField(max_length=10,null=True,db_column='profil_code')
    class Meta:
        # managed:False
        db_table = 'admin_profil'
    def __str__(self):
        return self.profil_descr
    

# *********************************************************************************************************** 
#                                               MODEL ACTEUR INFO
# *************************************************************************************************************
class acteur_infos(models.Model):
    ACTEUR_ID=models.AutoField(primary_key=True,db_column='ACTEUR_ID')
    STATUT_JURIDIQUE_ID=models.ForeignKey(acteur_statut_juridique, null=True,on_delete=models.CASCADE,db_column='STATUT_JURIDIQUE_ID')
    NOM=models.CharField(max_length=50,db_column="NOM")
    PRENOM=models.CharField(max_length=50,db_column="PRENOM")
    TELEPHONE=models.CharField(max_length=50,db_column="TELEPHONE")
    EMAIL=models.EmailField(max_length=50,db_column="EMAIL")
    PROFIL_ID=models.ForeignKey(admin_profil, null=True,on_delete=models.CASCADE,db_column='PROFIL_ID')
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=True,on_delete=models.CASCADE,db_column='COLLINE_ID')
    DATE_INSERTION=models.DateTimeField(auto_now_add=True,db_column="DATE_INSERTION")
    
    class Meta:
        db_table = 'acteur_infos'
         
    def __str__(self):
        return f"{self.NOM} {self.PRENOM}"
    
#***********************************************************************************************
#                                   MODEL ACTEUR INFO TRANSPORTEUR
# ********************************************              **************************************************
class acteur_infos_transporteur(models.Model):
    TRANSPORTEUR_ID=models.BigAutoField(primary_key=True,db_column='TRANSPORTEUR_ID')
    TYPE_VEHICULE_ID=models.ForeignKey(syst_type_vehicule, null=True,on_delete=models.SET_NULL,db_column='TYPE_VEHICULE_ID')
    CAPACITE_TRANSPORT=models.CharField(max_length=30, null=True,db_column='CAPACITE_TRANSPORT')
    LICENCE_TRANSPORT=models.FileField(max_length=255,upload_to="acteur_infos_transporteur/LICENCE_TRANSPORT",db_column="LICENCE_TRANSPORT")
    ACTEUR_ID=models.ForeignKey(acteur_infos,null=False,on_delete=models.CASCADE,db_column="ACTEUR_ID")
    
    class Meta: 
        # managed=False
        db_table = 'acteur_infos_transporteur'
    def __str__(self):
        return self.ACTEUR_ID.NOM

# ***************************************************************************************************
#                                  MODEL ADMIN USER
# ***************************************************************************************************
class admin_user(AbstractBaseUser,PermissionsMixin):
    id=models.BigAutoField(primary_key=True,db_column='id')
    email=models.EmailField(max_length=50,unique=True,null=False,db_column='email')
    telephone=models.CharField(max_length=30, null=True,db_column='telephone')
    password=models.CharField(max_length=100,null=False,db_column='password')
    profil_id=models.ForeignKey(admin_profil, null=True,on_delete=models.CASCADE,db_column='profil_id')
    is_active=models.SmallIntegerField(null=True,default=0,db_column='is_active')
    acteur_id=models.ForeignKey(acteur_infos,null=True,related_name="admin_user_act",on_delete=models.CASCADE,db_column="acteur_id")
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    last_login=None
    is_superuser=None

    objects = CustomUserManager()
    class Meta: 
        db_table = 'admin_users'
    def __str__(self):
        return self.email

# **************************************************************************************************************
#                                         MODEL CHAMP
# *************************************************************************************************************   
class acteur_champ(models.Model):
    CHAMP_ID=models.AutoField(primary_key=True,db_column='CHAMP_ID')
    COORD_POLY=models.TextField(null=True,db_column="COORD_POLY")
    CHAMP_DESC=models.CharField(max_length=50,null=False,db_column="CHAMP_DESC")
    SUPERFICIE=models.FloatField(null=True,db_column="SUPERFICIE")
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=True,on_delete=models.CASCADE,db_column='COLLINE_ID')
    ACTEUR_ID=models.ForeignKey(acteur_infos,null=False,on_delete=models.CASCADE,db_column="ACTEUR_ID")
    ID_FILIERE=models.ForeignKey(syst_filiere,null=False,on_delete=models.CASCADE,db_column="ID_FILIERE")
  
    class Meta:
        db_table = 'acteur_champ'
         
    def __str__(self):
        return self.CHAMP_DESC
# **************************************************************************************************************
#                                           MODEL ACTEUR MULTI SEMENCE 
# *************************************************************************************************************   
class acteur_multi_semence(models.Model):
    MULTI_ID=models.AutoField(primary_key=True,db_column='MULTI_ID')
    SEMENCE_ID=models.IntegerField(null=True,db_column="SEMENCE_ID")
    CAPACITE_MULTIPLICATION=models.FloatField(null=False,db_column="CAPACITE_MULTIPLICATION")
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=False,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=False,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=False,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=False,on_delete=models.CASCADE,db_column='COLLINE_ID')
    ACTEUR_ID=models.ForeignKey(acteur_infos,null=False,on_delete=models.CASCADE,db_column="ACTEUR_ID")
    UNITE_MESURE_ID=models.ForeignKey(syst_unite_mesure,null=False,on_delete=models.CASCADE,db_column="UNITE_MESURE_ID")
  
    class Meta:
        db_table = 'acteur_multi_semence'
         
    def __str__(self):
        return self.ACTEUR_ID.NOM