from .models import *
from .serializers import LineItemSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from rest_framework import status
from rest_framework import generics

"""
@api_view(['GET', 'POST'])
def Order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Order.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def line_item_list(request):
    if request.method == 'GET':
        Line_Items = Line_items.objects.all()
        serializer = LineItemSerializer(Line_Items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def line_item_detail(request, pk):
    try:
        line_item = Line_items.objects.get(pk=pk)
    except Line_items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LineItemSerializer(line_item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = LineItemSerializer(line_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        line_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LineItemListCreateView(generics.ListCreateAPIView):
    queryset = Line_items.objects.all()
    serializer_class = LineItemSerializer


class LineItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line_items.objects.all()
    serializer_class = LineItemSerializer
