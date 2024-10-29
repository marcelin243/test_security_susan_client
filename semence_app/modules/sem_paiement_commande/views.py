from .serialisers import *
from .models import sem_paiement_commande
from semence_app.modules.sem_commande_semence.models import sem_commande_semence
from semence_app.modules.sem_commande_semences_statut.models import sem_commande_semences_statut
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


#  VIEWS POUR USER MONITEUR TYPE
#===============================
class sem_paiement_commandeAPIView(viewsets.ModelViewSet):
    queryset = sem_paiement_commande.objects.all().order_by('PAIEMENT_ID')
    serializer_class_read=sem_paiement_commandeSerializers
    serializer_class_write=insert_sem_paiement_commandeSerializers
    
    filter_backends = [DjangoFilterBackend] # Ajouter le filtre DjangoFilterBackend
    # pagination_class=CustomPagination
    filterset_fields = ["COMMANDE_ID","MODE_PAIEMENT_ID"]  # Champs de filtrage
    
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write

    # Surcharge de la méthode perform_create pour ajouter la logique métier
    def perform_create(self, serializer):
        # Créer le paiement
        paiement = serializer.save()

        # Après avoir créé le paiement, mettre à jour le statut de la commande associée
        commande = paiement.COMMANDE_ID
        
        # Exemple : Mettre le statut à "Payé" (statut 2, par exemple)
        nouveau_statut = sem_commande_semences_statut.objects.get(pk=3)  # Statut "Payé"
        
        # Mise à jour du statut de la commande
        commande.STATUT_CMD_ID = nouveau_statut
        commande.save()