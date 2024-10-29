from rest_framework import serializers
from syst_app.models import syst_provinces

# SERIALIZERS  syst_provinces
# =====================================
class syst_provincesSerializers(serializers.ModelSerializer):
    class Meta:
        model=syst_provinces
        fields="__all__"      