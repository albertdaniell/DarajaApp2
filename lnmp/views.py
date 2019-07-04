from django.shortcuts import render

# Create your views here.



from rest_framework.generics import CreateAPIView
#from rest_framework.permissions import IsAdminUser
from lnmp.models import LNMP
from lnmp.serializers import LNMPSerializer

class LNMPApiView(CreateAPIView):
    queryset = LNMP.objects.all()
    serializer_class = LNMPSerializer
    # permission_classes = (IsAdminUser,)

    def create(self, request):
        print(request.data, "This is the request.data")
