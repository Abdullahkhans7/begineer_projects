from rest_framework import serializers
from .models import *


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_items
        fields = '__all__'

    def validate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Value must be greater than 0")


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
