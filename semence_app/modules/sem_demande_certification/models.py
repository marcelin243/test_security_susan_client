from django.db import models
from semence_app.modules.sem_stock_semence.models import sem_stock_semence
from semence_app.modules.sem_statut_certification.models import sem_statut_certification

# MODEL sem_demande_certification
# ==========================
class sem_demande_certification(models.Model):
    DEMANDE_ID=models.AutoField(primary_key=True,db_column='DEMANDE_ID')
    DATE_DEMANDE=models.DateTimeField(null=True,db_column="DATE_DEMANDE")
    DATE_DEMANDE = models.DateTimeField(auto_now_add=True, null=True, db_column="DATE_DEMANDE")
    STOCK_ID=models.ForeignKey(sem_stock_semence, null=True,on_delete=models.CASCADE,db_column='STOCK_ID')
    COMMENTAIRE=models.CharField(max_length=255,null=False,db_column="COMMENTAIRE")
    STATUT_DEMANDE_CERTIFICATION_ID=models.ForeignKey(sem_statut_certification, null=True,on_delete=models.CASCADE,db_column='STATUT_DEMANDE_CERTIFICATION_ID')

    
    class Meta:
        db_table = 'sem_demande_certification'
         
    def __str__(self):
        return str(self.DEMANDE_ID)