from rest_framework import serializers
from.models import *
class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Line_items
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'