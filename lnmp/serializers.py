from rest_framework import serializers
from lnmp.models import LipaNaMpesa
class LNMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = LipaNaMpesa
        fields = '__all__'