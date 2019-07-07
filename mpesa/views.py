from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mpesa.models import Mpesa
from mpesa.serializers import MpesaSerializer
from  mpesa.lipanampesa import lipa_na_mpesa

# Create your views here.
@csrf_exempt
def mpesa_list(request):
    """"
    List  all mpesa calls
    """
    if request.method =="GET":
        mpesas=Mpesa.objects.all()
        serializer=MpesaSerializer(mpesas,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer=MpesaSerializer(data=data)
        if serializer.is_valid():
            phone=data.phone_number
            amount=data.amount
            payBill=data.payBill
            lipa_na_mpesa(phone,amount,payBill)
            serializer.save()
            print(data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse (serializer.errors, status=400)

