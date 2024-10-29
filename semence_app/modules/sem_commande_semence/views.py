from .serialisers import *
from .models import sem_commande_semence
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from semence_app.modules.sem_commande_semence_details.models import sem_commande_semence_details
from semence_app.modules.sem_commande_semence_details.serialisers import *

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_commande_semenceAPIView(viewsets.ModelViewSet):
    queryset = sem_commande_semence.objects.all().order_by('-ID_COMMANDE')
    serializer_class_read=sem_commande_semenceSerializers
    serializer_class_write=insert_sem_commande_semenceSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["ID_PROPRIETAIRE","STATUT_CMD_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write

@api_view(["POST"])
def insert_sem_commande_semence(request):
    try:  
        data={
           "ID_PROPRIETAIRE":request.data.get("ID_PROPRIETAIRE"),
           "STATUT_CMD_ID" :request.data.get("STATUT_CMD_ID"),
           "MONTANT_TOTAL" :request.data.get("MONTANT_TOTAL")
        }
        serializercafe_commande_semance= insert_sem_commande_semenceSerializers(data=data)
        if serializercafe_commande_semance.is_valid(raise_exception=True):
            serializercafe_commande_semance.save()
            data_array=request.data.get("COMMANDES")
            for data_arrays in data_array:
                data_detail={
                   "MONTANT" :data_arrays['MONTANT'],
                   "QUANTITE" :data_arrays['QUANTITE_COMMANDE'],
                   "STOCK_ID" :data_arrays['STOCK_ID'],
                   "COMMANDE_ID" :serializercafe_commande_semance.instance.ID_COMMANDE,
                } 
                
                serializercafe_commande_semance_detail= insert_sem_commande_semence_detailsSerializers(data=data_detail)
                if serializercafe_commande_semance_detail.is_valid(raise_exception=True):
                    serializercafe_commande_semance_detail.save()
            return Response({"message": "Données enregistrées avec succès"}, status=status.HTTP_200_OK)
    except Exception as e :
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)         
  

    
