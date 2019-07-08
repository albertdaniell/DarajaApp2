# from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from lnmpOnline.models import LnmpOnline
# from lnmpOnline.serializers import LnmpOnlineSerializer

# # Create your views here.

# @csrf_exempt
# def lipanampesaonline(request):
#     """
#     List all trans
#     """
#     print(request.data)
#     if request.method == 'GET':
#         trans = LnmpOnline.objects.all()
#         serializer = LnmpOnlineSerializer(trans, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = LnmpOnlineSerializer(data=data)
#         if serializer.is_valid():
#             # print(data)
#             serializer.save()
#             print(data)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


from lnmpOnline.models import LnmpOnline
from lnmpOnline.serializers import LnmpOnlineSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from datetime import datetime



class LNMPList(CreateAPIView):
    permission_classes = [AllowAny]
    queryset=LnmpOnline.objects.all()
    serializer_class = LnmpOnlineSerializer
    """
    List all lnmp or create another lnmp
    """
    def create(self, request):
        # trans = LnmpOnline.objects.all()
        # serializer_class = LnmpOnlineSerializer(trans, many=True)
        # return Response(serializer_class.data)
        print("************************************************************************************************************************************************************************")

        print(request.data)
        serializer = LnmpOnlineSerializer(data=request.data)
        data=request.data
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

        

        

        # mpesa_data_callbk={
        #     "testcode":testcode,
        #     "MerchantRequestID":MerchantRequestID,
        #     "CheckoutRequestID":CheckoutRequestID,
        #     "ResultCode":ResultCode,
        #     "Amount":Amount,
        #     "mpesa_receipt_number":mpesa_receipt_number,
        #     "TransactionData":TransactionDate,
        #     "PhoneNumber":PhoneNumber
        # }

        print(TransactionDate)

        from lnmpOnline.models import LnmpOnline
        model=LnmpOnline.objects.create(
            checkoutRequestID=CheckoutRequestID,
            merchantRequestID=MerchantRequestID,
            resultCode=ResultCode,
            resultDesc=ResultDescription,
            transactionDate=TransactionDate,
            mpesaReceiptNumber=mpesa_receipt_number,        
            phoneNumber=PhoneNumber,
            amount=Amount

        )
        model.save()
        print("Data has been saved")

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     print("Has been saved to db")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     serializer = LnmpOnlineSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(request.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)