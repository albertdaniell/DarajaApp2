from django.shortcuts import render

# Create your views here.



from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from lnmp.models import LipaNaMpesa
from lnmp.serializers import LNMPSerializer
from datetime import datetime

class LNMPApiView(CreateAPIView):
    queryset = LipaNaMpesa.objects.all()
    serializer_class = LNMPSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print("This is the data received...")
        print(request.data, "This is the request.data")
        data=request.data

        testcode=(data['Body']['stkCallback']['ResultCode'])
        MerchantRequestID=(data['Body']['stkCallback']['MerchantRequestID'])
        CheckoutRequestID=(data['Body']['stkCallback']['CheckoutRequestID'])
        ResultCode = (data['Body']['stkCallback']['ResultCode'])
        ResultDescription = (data['Body']['stkCallback']['ResultDesc'])
        Amount=(data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])
        mpesa_receipt_number=(data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'])
        MpesaReceiptNumber=''
        TransactionDate=(data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value'])
        # convert date
        TransactionDate=str(TransactionDate)
        TransactionDate=datetime.strptime(TransactionDate,("%Y%m%d%H%M%S"))

        PhoneNumber=(data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'])

        # print(TransactionDate)

        mpesa_data_callbk={
            "testcode":testcode,
            "MerchantRequestID":MerchantRequestID,
            "CheckoutRequestID":CheckoutRequestID,
            "ResultCode":ResultCode,
            "Amount":Amount,
            "mpesa_receipt_number":mpesa_receipt_number,
            "TransactionData":TransactionDate,
            "PhoneNumber":PhoneNumber
        }

        print(TransactionDate)

        from lnmp.models import LipaNaMpesa
        model=LipaNaMpesa.objects.create(
            checkoutRequestID=CheckoutRequestID,
            merchantRequestID=MerchantRequestID,
            resultCode=ResultCode,
            resultDescription=ResultDescription,
            transactionDate=TransactionDate,
            phoneNumber=PhoneNumber,
            amount=Amount


        )
        model.save()

