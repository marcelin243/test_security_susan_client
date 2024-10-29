from django.db import models

# MODEL type_document
# ==========================
class type_document(models.Model):
    ID_TYPE_DOCUMENT=models.AutoField(primary_key=True,db_column='ID_TYPE_DOCUMENT')
    DESCRIPTION=models.CharField(max_length=255,null=False,db_column="DESCRIPTION")
    
    class Meta:
        db_table = 'type_document'
         
    def __str__(self):
        return self.DESCRIPTION