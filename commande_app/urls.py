
from django.urls import path,re_path
from rest_framework import routers
from commande_app.modules.com_commande_statut.views import com_commande_statutAPIView
from commande_app.modules.com_commande_statut_details.views import com_commande_statut_detailsAPIView
from commande_app.modules.com_commande_detail.views import com_commande_detailAPIView
from commande_app.modules.com_commande.views import com_commande_APIView
from commande_app.modules.com_paiement_commande.views import com_paiement_commandeAPIView

router=routers.DefaultRouter()
router.register("com_commande_statut",com_commande_statutAPIView)
router.register("com_commande_statut_details",com_commande_statut_detailsAPIView)
router.register("com_commande_detail",com_commande_detailAPIView)
router.register("com_commande",com_commande_APIView)
router.register("com_paiement_commande",com_paiement_commandeAPIView)

urlpatterns = [
   
    # path('logout/',logout ),
]