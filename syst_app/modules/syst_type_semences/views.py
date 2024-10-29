from .serialisers import syst_type_semencesSerializers
from syst_app.models import syst_type_semences
from rest_framework import viewsets

#  VIEWS POUR SYS TYPE SEMENCES
#===============================
class syst_type_semencesAPIView(viewsets.ModelViewSet):
    queryset = syst_type_semences.objects.all().order_by('TYPE_SEMENCE_DESC')
    serializer_class=syst_type_semencesSerializers
