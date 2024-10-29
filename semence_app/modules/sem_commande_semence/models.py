from django.db import models
from semence_app.modules.proprietaires.models import proprietaires
from semence_app.modules.sem_commande_semences_statut.models import sem_commande_semences_statut

# MODEL sem_commande_semence
# ==========================
class sem_commande_semence(models.Model):
    ID_COMMANDE=models.AutoField(primary_key=True,db_column='ID_COMMANDE')
    DATE_COMMANDE=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_COMMANDE")
    ID_PROPRIETAIRE=models.ForeignKey(proprietaires, null=True,on_delete=models.CASCADE,db_column='ID_PROPRIETAIRE')
    STATUT_CMD_ID=models.ForeignKey(sem_commande_semences_statut, null=True,on_delete=models.CASCADE,db_column='STATUT_CMD_ID')
    MONTANT_TOTAL=models.FloatField(null=True,db_column="MONTANT_TOTAL")

    
    class Meta:
        db_table = 'sem_commande_semence'
         
    def __str__(self):
        return str(self.ID_COMMANDE)