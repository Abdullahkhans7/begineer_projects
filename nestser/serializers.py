from rest_framework import serializers
from .models import *

class Authorserilizer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name','age']


class Bookserializer(serializers.serializer):
    class Meta:
        model=Book
        fields=['title','author','publish_date']