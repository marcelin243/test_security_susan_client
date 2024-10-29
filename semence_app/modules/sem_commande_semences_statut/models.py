from django.db import models

# MODEL sem_commande_semences_statut
# ==========================
class sem_commande_semences_statut(models.Model):
    STATUT_CMD_ID=models.AutoField(primary_key=True,db_column='STATUT_CMD_ID')
    STATUT_CMD_DESCR=models.CharField(max_length=255,null=False,db_column="STATUT_CMD_DESCR")
    
    class Meta:
        db_table = 'sem_commande_semences_statut'
         
    def __str__(self):
        return self.STATUT_CMD_DESCR