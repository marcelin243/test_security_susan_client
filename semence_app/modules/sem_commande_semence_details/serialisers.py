from rest_framework import serializers
from .models import sem_commande_semence_details
from semence_app.modules.sem_stock_semence.serialisers import sem_stock_semenceSerializers
from semence_app.modules.sem_commande_semence.serialisers import sem_commande_semenceSerializers
# SERIALIZERS  sem_commande_semence_details
# =====================================
class sem_commande_semence_detailsSerializers(serializers.ModelSerializer):
    STOCK_ID=sem_stock_semenceSerializers()
    COMMANDE_ID=sem_commande_semenceSerializers()
    class Meta:
        model=sem_commande_semence_details
        fields="__all__"    
          
class insert_sem_commande_semence_detailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=sem_commande_semence_details
        fields="__all__"      