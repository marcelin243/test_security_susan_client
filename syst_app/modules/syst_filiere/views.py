
from .serialisers import syst_filiereSerializers
from syst_app.models import syst_filiere
from rest_framework import viewsets
# va="rapha"

class syst_filiereAPIView(viewsets.ModelViewSet):
    queryset = syst_filiere.objects.all().order_by('NOM_FILIERE')
    serializer_class = syst_filiereSerializers
    # serializer_class = va