from django.db import models
from semence_app.modules.sem_commande_semence.models import sem_commande_semence
from semence_app.modules.sem_mode_paiement_commande.models import sem_mode_paiement_commande

# MODEL sem_paiement_commande
# ==========================
class sem_paiement_commande(models.Model):
    PAIEMENT_ID=models.AutoField(primary_key=True,db_column='PAIEMENT_ID')
    COMMANDE_ID=models.ForeignKey(sem_commande_semence, null=True,on_delete=models.CASCADE,db_column='COMMANDE_ID')
    MODE_PAIEMENT_ID=models.ForeignKey(sem_mode_paiement_commande, null=True,on_delete=models.CASCADE,db_column='MODE_PAIEMENT_ID')
    BANQUE=models.CharField(max_length=60,null=True,db_column="BANQUE")
    NUM_BORD=models.CharField(max_length=60,null=True,db_column="NUM_BORD")
    DATE_PAIEMENT=models.DateField(null=True,db_column="DATE_PAIEMENT")
    DATE_EXPIRATION=models.DateField(null=True,db_column="DATE_EXPIRATION")
    MONTANT=models.IntegerField(null=True,db_column="MONTANT")
    FICHIER=models.FileField(upload_to="sem_paiement_commande/file/",null=True,db_column="FICHIER")
    NUMERO_CARTE=models.CharField(max_length=60,null=True,db_column="NUMERO_CARTE")
    CVC=models.CharField(max_length=60,null=True,db_column="CVC")
    CODE_TRANSACTION=models.CharField(max_length=60,null=True,db_column="CODE_TRANSACTION")
    NUMERO_TRANSACTION=models.CharField(max_length=60,null=True,db_column="NUMERO_TRANSACTION")
    DATE_INSERTION=models.DateTimeField(auto_now_add=True,null=True,db_column="DATE_INSERTION")


    
    class Meta:
        db_table = 'sem_paiement_commande'
         
    def __str__(self):
        return str(self.PAIEMENT_ID)