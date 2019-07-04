from rest_framework import serializers
from mpesa.models import Mpesa

class MpesaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone_number = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `mpesa` instance, given the validated data.
        """
        return Mpesa.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        Update and return an existing `mpesa` instance, given the validated data.

        """
        instance.phone_number = validated_data.get('title', instance.title)
        
        instance.save()
        return instance
