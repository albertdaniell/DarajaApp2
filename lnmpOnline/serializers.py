from rest_framework import serializers
from lnmpOnline.models import LnmpOnline


class LnmpOnlineSerializer(serializers.Serializer):
    class Meta:
        model = LnmpOnline
        fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # checkoutRequestID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # merchantRequestID = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # resultCode = serializers.IntegerField(max_value=None, min_value=None)
    # resultDesc = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # amount = serializers.FloatField(max_value=None, min_value=None)
    # mpesaReceiptNumber = serializers.IntegerField(max_value=None, min_value=None)
    # transactionDate = serializers.DateTimeField(input_formats=None, default_timezone=None)
    # phoneNumber = serializers.CharField(required=False, allow_blank=True, max_length=100)



   

    # def create(self, validated_data):
    #     """
    #     Create and return a new  instance, given the validated data.
    #     """
    #     return LnmpOnline.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
       
    #     instance.save()
    #     return instance