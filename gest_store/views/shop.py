from gest_store.models.shop import Shop
from gest_store.serializers import ShopSerializer
from rest_framework import viewsets, permissions



class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
