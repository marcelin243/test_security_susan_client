
from semence_app.modules.type_proprietaire.views import type_proprietaireAPIView
from semence_app.modules.type_semences.views import type_semencesAPIView
from semence_app.modules.categorie_personne_morale.views import categorie_personne_moraleAPIView
from semence_app.modules.type_document.views import type_documentAPIView
from semence_app.modules.proprietaires.views import proprietairesAPIView
from semence_app.modules.filieres.views import filieresAPIView
from semence_app.modules.ch_variete.views import ch_varieteAPIView
from semence_app.modules.sem_stock_semence.views import sem_stock_semenceAPIView
from semence_app.modules.sem_commande_semences_statut.views import sem_commande_semences_statutAPIView
from semence_app.modules.sem_commande_semence.views import sem_commande_semenceAPIView,insert_sem_commande_semence
from semence_app.modules.sem_commande_semence_details.views import sem_commande_semence_detailsAPIView
from semence_app.modules.sem_statut_certification.views import sem_statut_certificationAPIView
from semence_app.modules.sem_demande_certification.views import sem_demande_certificationAPIView
from semence_app.modules.sem_certification_activite.views import sem_certification_activiteAPIView
from semence_app.modules.plantation.views import plantationAPIView
from semence_app.modules.champs.views import champsAPIView
from semence_app.modules.sem_mode_paiement_commande.views import sem_mode_paiement_commandeAPIView
from semence_app.modules.sem_paiement_commande.views import sem_paiement_commandeAPIView
from semence_app.modules.validation_paiement.views import UpdateStatutCommandeAPIView

from django.urls import path,re_path
from rest_framework import routers

router=routers.DefaultRouter()
router.register("type_proprietaire",type_proprietaireAPIView)
router.register("type_semences",type_semencesAPIView)
router.register("categorie_personne_morale",categorie_personne_moraleAPIView)
router.register("type_document",type_documentAPIView)
router.register("proprietaires",proprietairesAPIView)
router.register("filieres",filieresAPIView)
router.register("ch_variete",ch_varieteAPIView)
router.register("sem_stock_semence",sem_stock_semenceAPIView)
router.register("sem_commande_semences_statut",sem_commande_semences_statutAPIView)
router.register("sem_commande_semence",sem_commande_semenceAPIView)
router.register("sem_commande_semence_details",sem_commande_semence_detailsAPIView)
router.register("sem_statut_certification",sem_statut_certificationAPIView)
router.register("sem_demande_certification",sem_demande_certificationAPIView)
router.register("sem_certification_activite",sem_certification_activiteAPIView)
router.register("plantation",plantationAPIView)
router.register("champs",champsAPIView)
router.register("sem_mode_paiement_commande",sem_mode_paiement_commandeAPIView)
router.register("sem_paiement_commande",sem_paiement_commandeAPIView) 


urlpatterns = [
   
    path('insert_sem_commande_semence/',insert_sem_commande_semence,name="insert_sem_commande_semence" ),
    path('update_commande_statut/', UpdateStatutCommandeAPIView.as_view(), name='update_commande_statut'),

   
]
