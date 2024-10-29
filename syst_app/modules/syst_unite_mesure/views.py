
from .serialisers import syst_unite_mesureSerializers
from syst_app.models import syst_unite_mesure
from rest_framework import viewsets

class syst_unite_mesureAPIView(viewsets.ModelViewSet):
    queryset = syst_unite_mesure.objects.all().order_by('UNITE_MESURE_DESCR')
    serializer_class = syst_unite_mesureSerializers