from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lnmpOnline.models import LnmpOnline
from lnmpOnline.serializers import LnmpOnlineSerializer

# Create your views here.

@csrf_exempt
def lipanampesaonline(request):
    """
    List all trans
    """
    if request.method == 'GET':
        trans = LnmpOnline.objects.all()
        print(request.data)
        serializer = LnmpOnlineSerializer(trans, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LnmpOnlineSerializer(data=data)
        if serializer.is_valid():
            # print(data)
            serializer.save()
            print(request.data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
