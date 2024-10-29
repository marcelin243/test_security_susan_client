from django.db import models
from user_app.models import admin_user
from syst_app.models import syst_filiere
from syst_app.models import syst_mode_paiement

# ********************************************************************************
# COMMANDE STATUT
# *******************************************************************************
class com_commande_statut(models.Model):
    STATUT_COM_ID=models.BigAutoField(primary_key=True,db_column='STATUT_COM_ID') 
    STATUT_COM_DESCR=models.CharField(max_length=50,null=True,db_column='STATUT_COM_DESCR')
    class Meta:
        db_table = 'com_commande_statut'
    def __str__(self):
        return self.STATUT_COM_DESCR
    
# ********************************************************************************
#                               COMMANDE STATUT DETAIL
# *******************************************************************************
class com_commande_statut_details(models.Model):
    COM_STATUT_DET_ID=models.BigAutoField(primary_key=True,db_column='COM_STATUT_DET_ID') 
    COM_STATUT_DET_DESCR=models.CharField(max_length=50,null=True,db_column='COM_STATUT_DET_DESCR')
    class Meta:
        db_table = 'com_commande_statut_details'
    def __str__(self):
        return self.COM_STATUT_DET_DESCR
     
    

    
    
    
# ********************************************************************************
# COMMANDE                     COMMANDE                   COMMANDE
# *******************************************************************************
class com_commande(models.Model):
    COMMANDE_ID=models.BigAutoField(primary_key=True,db_column='COMMANDE_ID')
    USER_ID=models.ForeignKey(admin_user,null=True,on_delete=models.CASCADE,db_column="USER_ID")
    STATUT_COM_ID=models.ForeignKey(com_commande_statut,default=1,null=False,on_delete=models.CASCADE,db_column="STATUT_COM_ID")
    MONTANT_TOTAL=models.FloatField(null=True,db_column="MONTANT_TOTAL")
    class Meta:
        db_table = 'com_commande'
    def __str__(self):
        return str(self.COMMANDE_ID)
    
    
    
# ********************************************************************************
# COMMANDE DETAIL                 COMMANDE DETAIL                   COMMANDE DETAIL
# *******************************************************************************
class com_commande_detail(models.Model):
    COMMANDE_DETAIL_ID=models.BigAutoField(primary_key=True,db_column='COMMANDE_DETAIL_ID') 
    COMMANDE_ID=models.ForeignKey(com_commande,null=False,on_delete=models.CASCADE,db_column="COMMANDE_ID")
    QUANTITE=models.IntegerField(null=True,db_column="QUANTITE")
    PRIX_UNITAIRE=models.IntegerField(null=True,db_column="PRIX_UNITAIRE")
    STOCK_APPROV_ID=models.IntegerField(null=True,db_column="STOCK_APPROV_ID")
    COM_STATUT_DET_ID=models.ForeignKey(com_commande_statut_details,default=1,null=True,on_delete=models.CASCADE,db_column="COM_STATUT_DET_ID")
    SEMENCE_ID=models.IntegerField(null=True,db_column="SEMENCE_ID")
    SEMENCE_DESCR=models.CharField(max_length=100,null=False,db_column="SEMENCE_DESCR")
    HANGAR_ID=models.IntegerField(null=False,db_column="HANGAR_ID")
    HANGAR_DESCR=models.CharField(max_length=100,null=False,db_column="HANGAR_DESCR")
    ID_FILIERE=models.ForeignKey(syst_filiere,null=False,on_delete=models.CASCADE,db_column="ID_FILIERE")
    NOM_FILIERE=models.CharField(max_length=60,null=False,db_column="NOM_FILIERE")
    ID_CAT_SEMENCE=models.IntegerField(null=False,db_column="ID_CAT_SEMENCE")
    CAT_SEMENCES=models.CharField(max_length=60,null=False,db_column="CAT_SEMENCES")
    PROPRIETAIRE_NOM=models.CharField(max_length=150,null=True,db_column="PROPRIETAIRE_NOM")
    class Meta:
        db_table = 'com_commande_detail'
    def __str__(self):
        return str(self.COMMANDE_DETAIL_ID)
    
# *********************************************************************************************
# PAIEMENT COMMANDE                 PAIEMENT COMMANDE                  PAIEMENT COMMANDE
# *******************************************************************************
class com_paiement_commande(models.Model):
    PAIEMENT_ID=models.BigAutoField(primary_key=True,db_column='PAIEMENT_ID') 
    COMMANDE_ID=models.ForeignKey(com_commande_detail,null=False,on_delete=models.CASCADE,db_column="COMMANDE_ID")
    MODE_PAIEMENT_ID=models.ForeignKey(syst_mode_paiement,null=False,on_delete=models.CASCADE,db_column="MODE_PAIEMENT_ID")
    BANQUE=models.CharField(max_length=60,null=True,db_column="BANQUE")
    NUM_BORD=models.CharField(max_length=60,null=True,db_column="NUM_BORD")
    DATE_PAIEMENT=models.DateField(null=True,db_column="DATE_PAIEMENT")
    MONTANT=models.IntegerField(null=False,db_column="MONTANT")
    FICHIER=models.FileField(null=True,db_column="FICHIER",upload_to="com_paiement_commande/FICHIER")
    NUMERO_CARTE=models.CharField(max_length=60,null=True,db_column="NUMERO_CARTE")
    DATE_EXPIRATION=models.DateField(null=True,db_column="DATE_EXPIRATION")
    CVC=models.CharField(max_length=60,null=True,db_column="CVC")
    CODE_TRANSACTION=models.CharField(max_length=60,null=True,default="",db_column="CODE_TRANSACTION")
    NUMERO_TRANSACTION=models.CharField(max_length=60,null=False,db_column="NUMERO_TRANSACTION")
    DATE_INSERTION=models.DateTimeField(auto_now_add=True,db_column="DATE_INSERTION")
    class Meta:
        db_table = 'com_paiement_commande'
    def __str__(self):
        return str(self.BANQUE)
    