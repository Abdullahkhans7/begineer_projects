from django.shortcuts import render
from .models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Bookserializer

class Booklistview(APIView):
    def get(self,request):
        book = Book.objects.all()
        serializer=Bookserializer(book,many=True)
        return Response(serializer.data)