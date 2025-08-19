from gest_store.models.shopArticle import ShopArticle
from gest_store.serializers import ShopArticleSerializer
from rest_framework import viewsets, permissions


class ShopArticleViewSet(viewsets.ModelViewSet):
    queryset = ShopArticle.objects.all()
    serializer_class = ShopArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
