from .serialisers import filieresSerializers
from .models import filieres
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class filieresAPIView(viewsets.ModelViewSet):
    queryset = filieres.objects.all().order_by('NOM_FILIERE')
    serializer_class=filieresSerializers
