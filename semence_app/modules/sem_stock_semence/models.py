from django.db import models
from semence_app.modules.filieres.models import filieres
from semence_app.modules.ch_variete.models import ch_variete
from semence_app.modules.proprietaires.models import proprietaires
from semence_app.modules.type_semences.models import type_semences

# MODEL sem_stock_semence
# ==========================
class sem_stock_semence(models.Model):
    STOCK_ID=models.AutoField(primary_key=True,db_column='STOCK_ID')
    # CODE_VARIETE=models.CharField(max_length=50,null=True,db_column="CODE_VARIETE")
    # DESCRIPTION=models.CharField(max_length=80,null=True,db_column="DESCRIPTION")
    QUATITE=models.IntegerField(null=True,db_column="QUATITE")
    PRIX_UNITAIRE=models.IntegerField(null=True,db_column="PRIX_UNITAIRE")
    IS_ISABU=models.IntegerField(null=False,default=1,db_column="IS_ISABU")
    FILIERE_ID=models.ForeignKey(filieres, null=True,on_delete=models.CASCADE,db_column='FILIERE_ID')
    VARIETE_ID=models.ForeignKey(ch_variete, null=True,on_delete=models.CASCADE,db_column='VARIETE_ID')
    ID_PROPRIETAIRE=models.ForeignKey(proprietaires, null=True,on_delete=models.CASCADE,db_column='ID_PROPRIETAIRE')
    ID_TYPE_SEMENCES=models.ForeignKey(type_semences, null=True,on_delete=models.CASCADE,db_column='ID_TYPE_SEMENCES') 
    DATE_INSERTION=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_INSERTION")

    
    class Meta:
        db_table = 'sem_stock_semence'
         
    def __str__(self):
        return str(self.STOCK_ID)