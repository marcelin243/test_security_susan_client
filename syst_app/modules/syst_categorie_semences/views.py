from .serialisers import syst_categorie_semencesSerializers
from syst_app.models import syst_categorie_semences
from rest_framework import viewsets

#  VIEWS POUR CATEGORIE SEMENCE
#===============================
class syst_categorie_semencesAPIView(viewsets.ModelViewSet):
    queryset = syst_categorie_semences.objects.all().order_by('CAT_SEMENCES')
    serializer_class=syst_categorie_semencesSerializers
