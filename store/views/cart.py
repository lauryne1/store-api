from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from store.models.cart import Cart
from store.serializers.cart import CartSerializer
from rest_framework.permissions import IsAuthenticated



class CartListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailAPIView(APIView):
    def get(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
