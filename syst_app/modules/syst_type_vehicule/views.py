
from .serialisers import syst_type_vehiculeSerializers
from syst_app.models import syst_type_vehicule
from rest_framework import viewsets

class syst_type_vehiculeAPIView(viewsets.ModelViewSet):
    queryset = syst_type_vehicule.objects.all().order_by('TYPE_VEHICULE_DESC')
    serializer_class = syst_type_vehiculeSerializers