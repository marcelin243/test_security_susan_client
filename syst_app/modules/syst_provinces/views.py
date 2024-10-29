from .serialisers import syst_provincesSerializers
from syst_app.models import syst_provinces
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class syst_provincesAPIView(viewsets.ModelViewSet):
    queryset = syst_provinces.objects.all().order_by('PROVINCE_NAME')
    serializer_class=syst_provincesSerializers
