from django.db import models

# MODEL sem_certification_activite
# ==========================
class sem_certification_activite(models.Model):
    ACTIVITE_ID=models.AutoField(primary_key=True,db_column='ACTIVITE_ID')
    ACTIVITE_DESC=models.CharField(max_length=100,null=False,db_column="ACTIVITE_DESC")
    PRIX=models.IntegerField(null=True,db_column="PRIX")
    
    class Meta:
        db_table = 'sem_certification_activite'
         
    def __str__(self):
        return str(self.ACTIVITE_DESC)