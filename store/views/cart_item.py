from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from store.models.cart_item import CartItem
from store.serializers.cart_item import CartItemSerializer
from store.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated




class CartItemListCreateAPIView(APIView):
    def get(self, request):
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetailAPIView(APIView):
    permission_classes = [IsAuthenticated] # IsOwner

    def get(self, request, pk):
        item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = get_object_or_404(CartItem, pk=pk)
        serializer = CartItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = get_object_or_404(CartItem, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
