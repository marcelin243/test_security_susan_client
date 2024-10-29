from django.db import models

# MODEL sem_mode_paiement_commande
# ==========================
class sem_mode_paiement_commande(models.Model):
    MODE_PAIEMENT_ID=models.AutoField(primary_key=True,db_column='MODE_PAIEMENT_ID')
    MODE_PAIEMENT_DESCR=models.CharField(max_length=20,null=False,db_column="MODE_PAIEMENT_DESCR")
    
    class Meta:
        db_table = 'sem_mode_paiement_commande'
         
    def __str__(self):
        return self.MODE_PAIEMENT_DESCR