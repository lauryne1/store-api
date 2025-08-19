from gest_store.models import TransactionArticle
from gest_store.serializers import TransactionArticleSerializer
from rest_framework import viewsets, permissions


class TransactionArticleViewSet(viewsets.ModelViewSet):
    queryset = TransactionArticle.objects.all()
    serializer_class = TransactionArticleSerializer
    permission_classes = [permissions.IsAuthenticated]