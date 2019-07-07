from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from lnmp.models import LipaNaMpesa
from lnmp.serializers import LNMPSerializer
from datetime import datetime

# update
# BEGINING OF SAMPLE

# @csrf_exempt
# def lnmp_list(self,request):
#     """"
#     List  all mpesa calls
#     """
#     if request.method =="GET":
#         mpesas=LipaNaMpesa.objects.all()
#         serializer=LNMPSerializer(mpesas,many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method =="POST":
#         data = JSONParser().parse(request)
#         serializer=LNMPSerializer(data=data)
#         if serializer.is_valid():
#             print("This is the data received...")
#             print(request.data, "This is the request.data")
#             data=request.data

#             testcode=(data['Body']['stkCallback']['ResultCode'])
#             MerchantRequestID=(data['Body']['stkCallback']['MerchantRequestID'])
#             CheckoutRequestID=(data['Body']['stkCallback']['CheckoutRequestID'])
#             ResultCode = (data['Body']['stkCallback']['ResultCode'])
#             ResultDescription = (data['Body']['stkCallback']['ResultDesc'])
#             Amount=(data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])
#             mpesa_receipt_number=(data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'])
#             MpesaReceiptNumber=''
#             TransactionDate=(data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value'])
#             # convert date
#             TransactionDate=str(TransactionDate)
#             TransactionDate=datetime.strptime(TransactionDate,("%Y%m%d%H%M%S"))

#             PhoneNumber=(data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'])

#             # print(TransactionDate)

#             mpesa_data_callbk={
#                 "testcode":testcode,
#                 "MerchantRequestID":MerchantRequestID,
#                 "CheckoutRequestID":CheckoutRequestID,
#                 "ResultCode":ResultCode,
#                 "Amount":Amount,
#                 "mpesa_receipt_number":mpesa_receipt_number,
#                 "TransactionData":TransactionDate,
#                 "PhoneNumber":PhoneNumber
#             }

#             print(TransactionDate)
#             # serializer.save()
#             print(data)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse (serializer.errors, status=400)


# # END OF EXAMPLE

# ORIGINAL



class LNMPApiView(CreateAPIView):
    queryset = LipaNaMpesa.objects.all()
    serializer_class = LNMPSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print("God is great....")
        print("hehehe...This is the data received...")
        print(request.data, "This is the request.data")
        
        data=request.data
        # print(data)

        testcode=(data['Body']['stkCallback']['ResultCode'])
        print(testcode," This is the testcode")

        MerchantRequestID=(data['Body']['stkCallback']['MerchantRequestID'])
        print(MerchantRequestID, " This is the merchant request id")

        CheckoutRequestID=(data['Body']['stkCallback']['CheckoutRequestID'])
        print(CheckoutRequestID, " This is the checkout requst id")

        ResultCode = (data['Body']['stkCallback']['ResultCode'])
        print(ResultCode, " This is the result code")

        if ResultCode == 1032:
            print(" This mpesa Transaction was cancelled by user")
        elif ResultCode == 0:
            print("Niceeee, This was a successful transaction")
        elif ResultCode ==1:
            print("Sorry, you have insufficent funds!!!")

        ResultDescription = (data['Body']['stkCallback']['ResultDesc'])
        print(ResultDescription," This is the result desc")

        Amount=(data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])
        print(Amount," This is the amount")

        mpesa_receipt_number=(data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'])
        print(mpesa_receipt_number," This is the mpesa receipt")


        MpesaReceiptNumber=''
        TransactionDate=(data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value'])
        
        # convert date
        TransactionDate=str(TransactionDate)
        TransactionDate=datetime.strptime(TransactionDate,("%Y%m%d%H%M%S"))

        PhoneNumber=(data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'])
        print(PhoneNumber, "This is the phone number")

        

        

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
        print("Data has been saved")



# """


# {'Body': {'stkCallback': {'MerchantRequestID': '22498-6967453-1', 'CheckoutRequestID': 'ws_CO_DMZ_536008299_07072019073859321', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'NG723YFHWQ'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20190707073917}, {'Name': 'PhoneNumber', 'Value': 254791836987}]}}}}



# """
