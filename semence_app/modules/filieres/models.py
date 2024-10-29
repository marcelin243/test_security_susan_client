from django.db import models

# MODEL filieres
# ==========================
class filieres(models.Model):
    ID_FILIERE=models.AutoField(primary_key=True,db_column='ID_FILIERE')
    NOM_FILIERE=models.CharField(max_length=50,null=True,db_column="NOM_FILIERE")
    CODE_COULEUR=models.CharField(max_length=20,null=True,db_column="CODE_COULEUR")
    IMAGE=models.FileField(upload_to="filieres/file/",null=True,db_column="IMAGE")
    FICHE_TECHNIQUE=models.FileField(upload_to="filieres/file/",null=True,db_column="FICHE_TECHNIQUE")
    VALEUR_NORMALE_HS=models.FloatField(null=True,db_column="VALEUR_NORMALE_HS")
    VALEUR_NORMALE_TEMPERATURE=models.FloatField(null=True,db_column="VALEUR_NORMALE_TEMPERATURE")
    
    class Meta:
        db_table = 'filieres'
         
    def __str__(self):
        return self.NOM_FILIERE