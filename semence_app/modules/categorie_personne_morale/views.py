from .serialisers import categorie_personne_moraleSerializers
from .models import categorie_personne_morale
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class categorie_personne_moraleAPIView(viewsets.ModelViewSet):
    queryset = categorie_personne_morale.objects.all().order_by('DESCRI_CATEGORIE')
    serializer_class=categorie_personne_moraleSerializers
