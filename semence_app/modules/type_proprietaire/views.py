from .serialisers import type_proprietaireSerializers
from .models import type_proprietaire
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class type_proprietaireAPIView(viewsets.ModelViewSet):
    queryset = type_proprietaire.objects.all().order_by('DECRIPTION')
    serializer_class=type_proprietaireSerializers
