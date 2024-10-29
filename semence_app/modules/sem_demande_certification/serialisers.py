from rest_framework import serializers
from .models import sem_demande_certification

from semence_app.modules.sem_stock_semence.serialisers import sem_stock_semenceSerializers
from semence_app.modules.sem_statut_certification.serialisers import sem_statut_certificationSerializers

# SERIALIZERS  sem_demande_certification
# =====================================
class sem_demande_certificationSerializers(serializers.ModelSerializer):
    STOCK_ID=sem_stock_semenceSerializers()
    STATUT_DEMANDE_CERTIFICATION_ID=sem_statut_certificationSerializers()
    class Meta:
        model=sem_demande_certification
        fields="__all__"    
          
class insert_sem_demande_certificationSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_demande_certification
        fields="__all__"      