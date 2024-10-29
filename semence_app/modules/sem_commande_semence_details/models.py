from django.db import models
from semence_app.modules.sem_stock_semence.models import sem_stock_semence
from semence_app.modules.sem_commande_semence.models import sem_commande_semence

# MODEL sem_commande_semence_details
# ==========================
class sem_commande_semence_details(models.Model):
    ID_RELATION_COM=models.AutoField(primary_key=True,db_column='ID_RELATION_COM')
    # DATE_COMMANDE=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_COMMANDE")
    STOCK_ID=models.ForeignKey(sem_stock_semence, null=True,on_delete=models.CASCADE,db_column='STOCK_ID')
    COMMANDE_ID=models.ForeignKey(sem_commande_semence, null=True,on_delete=models.CASCADE,db_column='COMMANDE_ID')
    QUANTITE=models.IntegerField(null=True,db_column="QUANTITE")
    MONTANT=models.FloatField(null=True,db_column="MONTANT")

    
    class Meta:
        db_table = 'sem_commande_semence_details'
         
    def __str__(self):
        return str(self.ID_RELATION_COM)