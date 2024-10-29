from .serialisers import type_semencesSerializers
from .models import type_semences
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class type_semencesAPIView(viewsets.ModelViewSet):
    queryset = type_semences.objects.all().order_by('DESCR_SEMENCES')
    serializer_class=type_semencesSerializers
