from django.db import models
from semence_app.modules.plantation.models import plantation
from user_app.models import admin_user
from syst_app.models import *


# MODEL champs
# ==========================
class champs(models.Model):
    ID_CHAMP=models.AutoField(primary_key=True,db_column='ID_CHAMP')
    DESCR_CHAMP=models.CharField(max_length=100,null=True,db_column="DESCR_CHAMP")
    SUPERFICIE_CHAMP=models.FloatField(null=True,db_column="SUPERFICIE_CHAMP")
    ID_PLANTATION=models.ForeignKey(plantation, null=True,on_delete=models.CASCADE,db_column='ID_PLANTATION')
    COORD=models.TextField(null=True,db_column="COORD")
    COORD_POLY=models.TextField(null=True,db_column="COORD_POLY")
    CODE_CHAMP=models.CharField(max_length=10,null=True,db_column="CODE_CHAMP")
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=True,on_delete=models.CASCADE,db_column='COLLINE_ID')
    USER_ID=models.ForeignKey(admin_user, null=True,on_delete=models.CASCADE,db_column='USER_ID')
    
    class Meta:
        db_table = 'champs'
         
    def __str__(self):
        return self.DESCR_CHAMP