from .serialisers import syst_communesSerializers
from syst_app.models import syst_communes
from django_filters.rest_framework import DjangoFilterBackend as FB
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class syst_communesAPIView(viewsets.ModelViewSet):
    queryset = syst_communes.objects.all().order_by('COMMUNE_NAME')
    serializer_class=syst_communesSerializers
    filter_backends = [FB] 
    filterset_fields = ["PROVINCE_ID"]

