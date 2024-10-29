from django.db import models

# MODEL type_proprietaire
# ==========================
class type_proprietaire(models.Model):
    TYPE_PROPRIETAIRE_ID=models.AutoField(primary_key=True,db_column='TYPE_PROPRIETAIRE_ID')
    DECRIPTION=models.CharField(max_length=255,null=False,db_column="DECRIPTION")
    
    class Meta:
        db_table = 'type_proprietaire'
         
    def __str__(self):
        return self.DECRIPTION