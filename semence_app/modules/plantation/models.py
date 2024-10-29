from django.db import models
from semence_app.modules.proprietaires.models import proprietaires
from syst_app.models import *


# MODEL plantation
# ==========================
class plantation(models.Model):
    ID_PLANTATION=models.AutoField(primary_key=True,db_column='ID_PLANTATION')
    DESCRIPTION=models.CharField(max_length=255,null=True,db_column="DESCRIPTION")
    CODE_PLANTATION=models.CharField(max_length=10,null=True,db_column="CODE_PLANTATION")
    PROVINCE_ID=models.ForeignKey(syst_provinces, null=True,on_delete=models.CASCADE,db_column='PROVINCE_ID')
    COMMUNE_ID=models.ForeignKey(syst_communes, null=True,on_delete=models.CASCADE,db_column='COMMUNE_ID')
    ZONE_ID=models.ForeignKey(syst_zones, null=True,on_delete=models.CASCADE,db_column='ZONE_ID')
    COLLINE_ID=models.ForeignKey(syst_collines, null=True,on_delete=models.CASCADE,db_column='COLLINE_ID')
    IMAGE=models.FileField(upload_to="plantation/image/",null=True,db_column="IMAGE")
    ID_PROPRIETAIRE=models.ForeignKey(proprietaires, null=True,on_delete=models.CASCADE,db_column='ID_PROPRIETAIRE')
    DATE_INSERTION=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_INSERTION")
    SUPERFICIE=models.CharField(max_length=100,null=True,db_column="SUPERFICIE")
    CODE=models.CharField(max_length=11,null=True,db_column="CODE")
    ALTITUDE=models.SmallIntegerField(null=True,db_column="ALTITUDE")
    STATUT=models.SmallIntegerField(null=True,db_column="STATUT")
    ETAPE_ECOSYSTEME=models.SmallIntegerField(null=True,db_column="ETAPE_ECOSYSTEME")
    
    
    class Meta:
        db_table = 'plantation'
         
    def __str__(self):
        return self.DESCRIPTION