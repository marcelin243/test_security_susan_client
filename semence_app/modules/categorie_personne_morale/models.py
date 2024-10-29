from django.db import models

# MODEL categorie_personne_morale
# ==========================
class categorie_personne_morale(models.Model):
    CATEGORIE_ID=models.AutoField(primary_key=True,db_column='CATEGORIE_ID')
    DESCRI_CATEGORIE=models.CharField(max_length=255,null=False,db_column="DESCRI_CATEGORIE")
    
    class Meta:
        db_table = 'categorie_personne_morale'
         
    def __str__(self):
        return self.DESCRI_CATEGORIE