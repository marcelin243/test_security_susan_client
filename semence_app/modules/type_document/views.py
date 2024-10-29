from .serialisers import type_documentSerializers
from .models import type_document
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class type_documentAPIView(viewsets.ModelViewSet):
    queryset = type_document.objects.all().order_by('DESCRIPTION')
    serializer_class=type_documentSerializers
