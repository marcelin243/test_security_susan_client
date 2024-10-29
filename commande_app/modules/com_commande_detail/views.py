from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serialisers import *
import logging
from autres_modules.message import message
from commande_app.models import com_commande_detail
from syst_app.modules.producteur.producteur_mode_paiement import publish
from rest_framework.response import Response
from commande_app.modules.com_commande.serialisers import insert_com_commande_Serializers

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class com_commande_detailAPIView(viewsets.ModelViewSet):
    queryset = com_commande_detail.objects.all().order_by('COMMANDE_DETAIL_ID')
    serializer_class_read=jointure_com_commande_detail_Serializers
    serializer_class_write=insert_com_commande_detail_Serializers
    filter_backends = [DjangoFilterBackend]
    # pagination_class=CustomPagination
    filterset_fields = ["COM_STATUT_DET_ID","COMMANDE_ID","ID_FILIERE"]
    
    def create(self, request):
        
        list_detail = request.data.get("list_detail")
        if not list_detail:
            return Response({"detail": "Le détail de la commande est vide !!!"}, status=400)

    # Sérialisation et enregistrement de la commande principale
        data_commande = {
        "USER_ID": request.data.get("USER_ID"),
        "MONTANT_TOTAL": request.data.get("MONTANT_TOTAL")
    }
        serialiser_commande = insert_com_commande_Serializers(data=data_commande)
        serialiser_commande.is_valid(raise_exception=True)
        serialiser_commande.save()

        commande_id = serialiser_commande.instance.COMMANDE_ID
        liste_details_a_envoyer = []

        # Boucler sur les détails de la commande
        for detail in list_detail:
            detail["COMMANDE_ID"] = commande_id
            serialiser_detail = insert_com_commande_detail_Serializers(data=detail)
            serialiser_detail.is_valid(raise_exception=True)
            serialiser_detail.save()

            commande_detail_id = serialiser_detail.instance.COMMANDE_DETAIL_ID

            # Préparer chaque détail et l'ajouter à la liste à envoyer
            data_ = {
            "ID_STOCK_APPRO": detail["ID_STOCK_APPRO"],
            "QTE": detail["QUANTITE"],
            "PRIX": detail["PRIX_UNITAIRE"],
            "NOM_CLIENT": detail["NOM_CLIENT"],
            "PRENOM_CLIENT": detail["PRENOM_CLIENT"],
            "ID_CLIENT": detail["ID_CLIENT"],
            "ID_COMMANDE_DETAIL": commande_detail_id,
            "ID_COMMANDE": commande_id,
            "MONTANT_TOTAL": request.data.get("MONTANT_TOTAL"),
        }
            liste_details_a_envoyer.append(data_)

    # Envoyer la liste complète à RabbitMQ en une seule fois
        self.publish_to_rabbitmq("insert_detail", liste_details_a_envoyer, "detail_commande_key")

        return Response({"message": "Commande et détails enregistrés avec succès"}, status=201)
    
    
    def publish_to_rabbitmq(self, content_type, data, routing_key):
        """
        Publier une liste de données ou un message unique sur RabbitMQ.
        """
        try:
            publish(content_type, data, routing_key)  # data peut être une liste complète
            logging.info(f"Données publiées avec succès sur {routing_key}")
        except Exception as e:
            logging.error(f"Erreur lors de la publication sur RabbitMQ : {e}")
            raise Exception(f"Erreur lors de la publication sur RabbitMQ : {e}")


    
    # def create(self, request):
    #     list_detail=request.data.get("list_detail")
    #     if list_detail is None:
    #         return Response({"detail":"le detail commande est vide !!!"})
    #     data={"USER_ID":request.data.get("USER_ID"),"MONTANT_TOTAL":request.data.get("MONTANT_TOTAL")}
    #     serialiser=insert_com_commande_Serializers(data=data)
    #     serialiser.is_valid(raise_exception=True)
    #     serialiser.save()
    #     inst=serialiser.instance.COMMANDE_ID
                
    #     for detail in list_detail:
    #         detail["COMMANDE_ID"]=inst
    #         serialiser=insert_com_commande_detail_Serializers(data=detail)
    #         serialiser.is_valid(raise_exception=True)
    #         serialiser.save()
    #         inst_hist=serialiser.instance.COMMANDE_DETAIL_ID
    #         data_={
    #             "ID_STOCK_APPRO":detail["ID_STOCK_APPRO"],
    #             "QTE":detail["QUANTITE"],
    #             "PRIX":detail["PRIX_UNITAIRE"],
    #             "NOM_CLIENT":detail["NOM_CLIENT"],
    #             "PRENOM_CLIENT":detail["PRENOM_CLIENT"] ,
    #             "ID_CLIENT":detail["ID_CLIENT"],
    #             "ID_COMMANDE_DETAIL":inst_hist,
    #             "ID_COMMANDE":inst_hist,
    #             "MONTANT_TOTAL":request.data.get("MONTANT_TOTAL"),
    #         }
            
    #         publish("insert_detail",data_,"detail_commande_key")
    #     return Response(message("save"))
    
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     publish("update_detail",{"COMMANDE_DETAIL_ID":serializer.instance.COMMANDE_DETAIL_ID,"COM_STATUT_DET_ID":request.data.get("COM_STATUT_DET_ID")},"detail_commande_key")
    #     return Response(serializer.data)

    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write