from django.db import models

# MODEL sem_statut_certification
# ==========================
class sem_statut_certification(models.Model):
    STATUT_DEMANDE_CERTIFICATION_ID=models.AutoField(primary_key=True,db_column='STATUT_DEMANDE_CERTIFICATION_ID')
    STATUT_DEMANDE_CERTIFICATION_DESCR=models.CharField(max_length=255,null=False,db_column="STATUT_DEMANDE_CERTIFICATION_DESCR")
    
    class Meta:
        db_table = 'sem_statut_certification'
         
    def __str__(self):
        return self.STATUT_DEMANDE_CERTIFICATION_DESCR