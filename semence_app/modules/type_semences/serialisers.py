from rest_framework import serializers
from .models import type_semences

# SERIALIZERS  type_semences
# =====================================
class type_semencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=type_semences
        fields="__all__"      