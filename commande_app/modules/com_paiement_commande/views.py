

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serialisers import *
from commande_app.modules.com_commande.serialisers import insert_com_commande_Serializers
from commande_app.models import * 
from commande_app.modules.com_commande_detail.serialisers import *
from autres_modules.message import message
from syst_app.modules.producteur.producteur_mode_paiement import publish
from rest_framework.response import Response
from rest_framework import status
import json

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class com_paiement_commandeAPIView(viewsets.ModelViewSet):
    queryset = com_paiement_commande.objects.all().order_by('PAIEMENT_ID')
    serializer_class_read=jointure_com_paiement_commande_Serializers
    serializer_class_write=insert_com_paiement_commande_Serializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["COMMANDE_ID","MODE_PAIEMENT_ID"]
    
    def create(self, request):
        serialiser=insert_com_paiement_commande_Serializers(data=request.data)
        serialiser.save() if serialiser.is_valid() else serialiser.errors
        dann=serialiser.data.copy()
        list_commande_payer=json.loads(request.data.get("list_commande_payer"))
        dann["list_commande_payer"]=list_commande_payer
        dann=dict(dann)
        try: 
            list_commande_detail_obj=com_commande_detail.objects.filter(COMMANDE_DETAIL_ID__in=list_commande_payer)
            for detail_payer in list_commande_detail_obj:
                ser=insert_com_commande_detail_Serializers(detail_payer,data={"COM_STATUT_DET_ID":3},partial=True)
                ser.is_valid(raise_exception=True)
                ser.save()
                
                publish("insert_paiement_update_detail",dann,"detail_commande_key")
            return Response(message("save"))   
        except com_commande.DoesNotExist:
            return Response(message("not_found",val="commande"))
         
    # ===========================================
    # FONCTION POUR DECALER ENTRE LES SERIALIZERS
    # ===========================================
    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return self.serializer_class_read
        return self.serializer_class_write
    
        
   
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     publish("update_detail",{"COMMANDE_DETAIL_ID":serializer.instance.COMMANDE_DETAIL_ID,"COM_STATUT_DET_ID":request.data.get("COM_STATUT_DET_ID")},"detail_commande_key")
    #     return Response(serializer.data)

    
    
    # data={
        #     "COMMANDE_ID":int(request.data.get("COMMANDE_ID")),
        #     "MODE_PAIEMENT_ID":int(request.data.get("MODE_PAIEMENT_ID")),
        #     "BANQUE":request.data.get("BANQUE"),
        #     "NUM_BORD":request.data.get("NUM_BORD"),
        #     "DATE_PAIEMENT":request.data.get("DATE_PAIEMENT"),
        #     "MONTANT":int(request.data.get("MONTANT")),
        #     "NUMERO_CARTE":request.data.get("NUMERO_CARTE"),
        #     "DATE_EXPIRATION":request.data.get("DATE_EXPIRATION"),
        #     "CVC":request.data.get("CVC"),
        #     "CODE_TRANSACTION":request.data.get("CODE_TRANSACTION"),
        #     "NUMERO_TRANSACTION":request.data.get("NUMERO_TRANSACTION"),
        #     "FICHIER":request.FILES.get("FICHIER"),
        # }
    
    
    
