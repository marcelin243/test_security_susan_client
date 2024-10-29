
from .serialisers import insert_syst_mode_paiement_Serializers as serializer_mode_pay
from syst_app.models import syst_mode_paiement
from rest_framework import viewsets
from syst_app.modules.producteur.producteur_mode_paiement import publish
from rest_framework.response import Response
class syst_mode_paiementAPIView(viewsets.ModelViewSet):
    queryset = syst_mode_paiement.objects.all().order_by('MODE_PAIEMENT_DESCR')
    serializer_class = serializer_mode_pay
    # ===========================================
    def create(self,request):
        serialiser=serializer_mode_pay(data=request.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        publish("mode_paiement_created",serialiser.data,"test_cle")
        return Response({"detail":"save"})
     
    # def perform_create(self, serialiser):
    #     publish("mode_paiement_created",serialiser.data)pyth
    #     print("===========================================================================================")
    #     print(serialiser.data)
    #     print("===========================================================================================")
        
    
    def update(self,request,pk):
        ob=syst_mode_paiement.objects.get(MODE_PAIEMENT_ID=pk)
        print("UPDATED")
        serialiser=serializer_mode_pay(ob,data={"MODE_PAIEMENT_DESCR":"KMR92222RAPHA2"},partial=True)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        print(serialiser.data)
        publish("mode_paiement_update",serialiser.data)
        return Response({"detail":"update"})