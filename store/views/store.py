from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from store.models import Store
from store.serializers import StoreSerializer


class StoreListCreateAPIView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailAPIView(APIView):
    def get(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
