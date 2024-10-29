
from user_app.modules.admin_user.views import create_admin ,logout, login_admin,admin_userAPIView,change_password_admin
from user_app.modules.admin_profil_user.views import admin_profilAPIView
from user_app.modules.acteur_statut_juridique.views import acteur_statut_juridiqueAPIView
from user_app.modules.acteur_infos_transporteur.views import acteur_infos_transporteurAPIView
from user_app.modules.acteur_infos.views import acteur_infosAPIView
from user_app.modules.acteur_champ.views import acteur_champAPIView
from user_app.modules.acteur_multi_semence.views import acteur_multi_semenceAPIView
from user_app.modules.insert_acteur import insert_acteur,insert_transporteur
from rest_framework_simplejwt.views import TokenRefreshView
from user_app.modules.admin_user.views import CustomTokenObtainPairView

from django.urls import path,re_path
from rest_framework import routers

router=routers.DefaultRouter()
router.register("admin_profil",admin_profilAPIView)
router.register("admin_user",admin_userAPIView)
router.register("acteur_statut_juridique",acteur_statut_juridiqueAPIView)
router.register("acteur_infos",acteur_infosAPIView)
router.register("acteur_champ",acteur_champAPIView)
router.register("acteur_infos_transporteur",acteur_infos_transporteurAPIView)
router.register("acteur_multi_semence",acteur_multi_semenceAPIView)



urlpatterns = [
   
    path('logout/',logout ),
    path('login_admin/',login_admin ),
    path('create_admin/',create_admin ),
    path('change_password_admin/',change_password_admin ),
    path('insert_acteur/',insert_acteur ),
    path('insert_transporteur/',insert_transporteur ),
    
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]