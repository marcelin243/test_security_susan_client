from rest_framework import serializers
from .models import type_document

# SERIALIZERS  type_document
# =====================================
class type_documentSerializers(serializers.ModelSerializer):
    class Meta:
        model=type_document
        fields="__all__"      