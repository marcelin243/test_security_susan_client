
from syst_app.modules.syst_type_semences.views import syst_type_semencesAPIView
from syst_app.modules.syst_categorie_semences.views import syst_categorie_semencesAPIView
from syst_app.modules.syst_semences.views import syst_semencesAPIView
from syst_app.modules.syst_filiere.views import syst_filiereAPIView
from syst_app.modules.syst_collines.views import syst_collinesAPIView
from syst_app.modules.syst_communes.views import syst_communesAPIView
from syst_app.modules.syst_provinces.views import syst_provincesAPIView
from syst_app.modules.syst_zones.views import syst_zonesAPIView
from syst_app.modules.syst_type_vehicule.views import syst_type_vehiculeAPIView
from syst_app.modules.syst_unite_mesure.views import syst_unite_mesureAPIView
from syst_app.modules.syst_mode_paiement.views import syst_mode_paiementAPIView
from django.urls import path,re_path
from rest_framework import routers

router=routers.DefaultRouter()
router.register("syst_type_semences",syst_type_semencesAPIView)
router.register("syst_categorie_semences",syst_categorie_semencesAPIView)
router.register("syst_semences",syst_semencesAPIView)
router.register("syst_filiere",syst_filiereAPIView)
router.register("syst_collines",syst_collinesAPIView)
router.register("syst_communes",syst_communesAPIView)
router.register("syst_provinces",syst_provincesAPIView)
router.register("syst_zones",syst_zonesAPIView)
router.register("syst_type_vehicule",syst_type_vehiculeAPIView)
router.register("syst_unite_mesure",syst_unite_mesureAPIView)
router.register("syst_mode_paiement",syst_mode_paiementAPIView)

urlpatterns = [
   
  
                ]
