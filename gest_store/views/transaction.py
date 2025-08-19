from gest_store.models import TransactionArticle
from gest_store.models.transaction import Transaction
from gest_store.serializers import TransactionArticleSerializer, TransactionSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action # type: ignore



class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme client si non spécifié
        serializer.save(client=self.request.user)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def articles(self, request, pk=None):
        # Récupérer les articles d'une transaction spécifique
        transaction = self.get_object()
        transaction_articles = TransactionArticle.objects.filter(transaction=transaction)
        serializer = TransactionArticleSerializer(transaction_articles, many=True)
        return Response(serializer.data)