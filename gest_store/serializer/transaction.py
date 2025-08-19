from gest_store import serializers
from gest_store.models import TransactionArticle
from gest_store.models.article import Article
from gest_store.models.transaction import Transaction
from gest_store.models.utilisateur import Utilisateur
from gest_store.serializer.article import ArticleSerializer
from gest_store.serializer.shop import ShopSerializer
from gest_store.serializer.utilisateur import UtilisateurSerializer

class TransactionSerializer(serializers.ModelSerializer):
    client = UtilisateurSerializer(read_only=True)
    shop = ShopSerializer(read_only=True)
    articles = serializers.TransactionArticleSerializer(many=True, read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Utilisateur.objects.all(), source='client', write_only=True
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        queryset=Shop.objects.all(), source='shop', write_only=True
    )

    class Meta:
        model = Transaction
        fields = ['id', 'client', 'client_id', 'shop', 'shop_id', 'amount', 'transaction_date', 'articles']
        read_only_fields = ['transaction_date', 'articles']

    def create(self, validated_data):
        # Créer une transaction et associer des articles
        articles_data = self.context['request'].data.get('articles', [])
        transaction = Transaction.objects.create(
            client=validated_data['client'],
            shop=validated_data['shop'],
            amount=validated_data['amount']
        )
        for article_data in articles_data:
            TransactionArticle.objects.create(
                transaction=transaction,
                article_id=article_data['article_id'],
                quantite=article_data['quantite'],
                prix_unitaire=article_data['prix_unitaire']
            )
        return transaction