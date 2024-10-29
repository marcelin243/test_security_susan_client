
from .serialisers import acteur_statut_juridiqueSerializers
from user_app.models import acteur_statut_juridique
from rest_framework import viewsets

class acteur_statut_juridiqueAPIView(viewsets.ModelViewSet):
    queryset = acteur_statut_juridique.objects.all().order_by('STATUT_JURIDIQUE_DESC')
    serializer_class = acteur_statut_juridiqueSerializers