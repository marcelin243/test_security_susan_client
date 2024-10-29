from django.db import models
from semence_app.modules.filieres.models import filieres

# MODEL ch_variete
# ==========================
class ch_variete(models.Model):
    VARIETE_ID=models.AutoField(primary_key=True,db_column='VARIETE_ID')
    CODE_VARIETE=models.CharField(max_length=50,null=True,db_column="CODE_VARIETE")
    DESCRIPTION=models.CharField(max_length=80,null=True,db_column="DESCRIPTION")
    ID_FILIERE=models.ForeignKey(filieres, null=True,on_delete=models.CASCADE,db_column='ID_FILIERE')
    PATH_IMAGE1=models.FileField(upload_to="ch_variete/file/",null=True,db_column="PATH_IMAGE1")
    PATH_IMAGE2=models.FileField(upload_to="ch_variete/file/",null=True,db_column="PATH_IMAGE2")
    PATH_IMAGE3=models.FileField(upload_to="ch_variete/file/",null=True,db_column="PATH_IMAGE3")
    PATH_IMAGE4=models.FileField(upload_to="ch_variete/file/",null=True,db_column="PATH_IMAGE4")

    
    class Meta:
        db_table = 'ch_variete'
         
    def __str__(self):
        return str(self.VARIETE_ID)