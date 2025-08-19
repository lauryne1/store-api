from gest_store.serializer.article import ArticleSerializer
from gest_store.serializer.shop import ShopSerializer
from gest_store.serializer.utilisateur import UtilisateurSerializer
from rest_framework import serializers
from .models import Utilisateur, Categorie, Shop, Article, ShopArticle, Transaction, TransactionArticle
from django.contrib.auth import get_user_model


class TransactionArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source='article', write_only=True
    )
    sous_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = TransactionArticle
        fields = ['id', 'transaction', 'article', 'article_id', 'quantite', 'prix_unitaire', 'sous_total']
        read_only_fields = ['transaction', 'sous_total']

class TransactionSerializer(serializers.ModelSerializer):
    client = UtilisateurSerializer(read_only=True)
    shop = ShopSerializer(read_only=True)
    articles = TransactionArticleSerializer(many=True, read_only=True)
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