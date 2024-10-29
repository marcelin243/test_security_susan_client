from .serialisers import syst_zonesSerializers
from syst_app.models import syst_zones
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend as FB

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class syst_zonesAPIView(viewsets.ModelViewSet):
    queryset = syst_zones.objects.all().order_by('ZONE_NAME')
    serializer_class=syst_zonesSerializers
    filter_backends = [FB] 
    filterset_fields = ["COMMUNE_ID"]
