from rest_framework import serializers
from lnmp.models import LNMP
class LNMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMP
        