from django.db import models

# MODEL type_semences
# ==========================
class type_semences(models.Model):
    ID_TYPE_SEMENCES=models.AutoField(primary_key=True,db_column='ID_TYPE_SEMENCES')
    DESCR_SEMENCES=models.CharField(max_length=255,null=False,db_column="DESCR_SEMENCES")
    
    class Meta:
        db_table = 'type_semences'
         
    def __str__(self):
        return self.DESCR_SEMENCES