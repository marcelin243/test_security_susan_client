from rest_framework import serializers
from syst_app.models import syst_type_semences

# SERIALIZERS  syst_type_semences
# =====================================
class syst_type_semencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_type_semences
        fields="__all__"      