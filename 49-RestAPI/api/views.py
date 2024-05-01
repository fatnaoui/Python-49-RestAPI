from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers,models
import json

class Student:
    def __init__(self,name,id,mark) -> None:
        self.name=name
        self.id=id
        self.mark=mark

@api_view()
def apiarticle(request):
    articles=models.Article.objects.all()
    response=serializers.ArticleSerializer(articles,many=True)
    return Response(response.data)

@api_view(['POST'])
def createarticleapi(request):
    body = json.loads(request.body)
    response = serializers.ArticleSerializer(data=body)
    if response.is_valid():
        instance=response.save()
        response = serializers.ArticleSerializer(instance)
        return Response(response.data)
    return Response(response.errors)

# api_view handles the httprequests
@api_view()
def usersApi(request):
    student1=Student("hamza",1,100)
    student2=Student("billal",2,200)
    student3=Student("primo",3,300)
    response=serializers.StudentSerializer([
        student1,
        student2,
        student3
    ],many=True)  # tell that you're sending multiple object  
    return Response(response.data)

