from .serialisers import syst_collinesSerializers
from syst_app.models import syst_collines
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend as FB
#  VIEWS POUR USER MONITEUR TYPE
#===============================
class syst_collinesAPIView(viewsets.ModelViewSet):
    queryset = syst_collines.objects.all().order_by('COLLINE_ID')
    serializer_class=syst_collinesSerializers
    filter_backends = [FB] 
    filterset_fields = ["ZONE_ID"]
    
