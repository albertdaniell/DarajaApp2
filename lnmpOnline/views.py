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


class LNMPList(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LnmpOnlineSerializer
    """
    List all lnmp or create another lnmp
    """
    def create(self, request, format=None):
        trans = LnmpOnline.objects.all()
        serializer_class = LnmpOnlineSerializer(trans, many=True)
        return Response(serializer_class.data)
        print("************************************************************************************************************************************************************************")

        print(request.data)

    # def post(self, request, format=None):
    #     serializer = LnmpOnlineSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(request.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)