# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from semence_app.modules.sem_commande_semence.models import sem_commande_semence
from semence_app.modules.sem_commande_semences_statut.models import sem_commande_semences_statut
from semence_app.modules.validation_paiement.serialisers import UpdateStatutCommandeSerializer
from semence_app.modules.sem_commande_semence_details.models import sem_commande_semence_details
from semence_app.modules.sem_stock_semence.serialisers import insert_sem_stock_semenceSerializers
from semence_app.modules.sem_stock_semence.models import sem_stock_semence

class UpdateStatutCommandeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        commande_id = request.data.get("commande_id")
        
        try:
            # Récupérer la commande en utilisant l'ID de commande
            commande = sem_commande_semence.objects.get(ID_COMMANDE=commande_id)
            # Récupérer l'instance de sem_commande_semences_statut correspondant à l'ID 4
            statut_paye = sem_commande_semences_statut.objects.get(STATUT_CMD_ID=4)
            
            # Assigner l'instance de statut au champ STATUT_CMD_ID
            commande.STATUT_CMD_ID = statut_paye
            commande.save()
            detail=sem_commande_semence_details.objects.filter(COMMANDE_ID=commande_id)
            for com in detail:
                sem=sem_stock_semence.objects.get(STOCK_ID=com.STOCK_ID.STOCK_ID)
                DATA={
                    "PRIX_UNITAIRE":0,
                    "FILIERE_ID":sem.FILIERE_ID.ID_FILIERE,
                    "QUATITE":com.QUANTITE,
                    "ID_PROPRIETAIRE":commande.ID_PROPRIETAIRE.ID_PROPRIETAIRE,
                    "ID_TYPE_SEMENCES":sem.ID_TYPE_SEMENCES.ID_TYPE_SEMENCES,
                    "VARIETE_ID":sem.VARIETE_ID.VARIETE_ID,
                    "IS_ISABU":0,
                    
                }
                SER=insert_sem_stock_semenceSerializers(data=DATA)
                SER.is_valid(raise_exception=True)
                SER.save()
            
            return Response({"status": "Statut mis à jour avec succès"})
        except sem_commande_semence.DoesNotExist:
            return Response({"error": "Commande non trouvée"}, status=404)
        except sem_commande_semences_statut.DoesNotExist:
            return Response({"error": "Statut non trouvé"}, status=404)
        


     