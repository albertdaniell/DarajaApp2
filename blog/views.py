from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.models import Blog
from blog.serializers import BlogSerializer

# Create your views here.
@csrf_exempt
def blog_list(request):
    """"
    List  all blogs
    """
    if request.method =="GET":
        blogs=Blog.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer=BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse (serializer.errors, status=400)

