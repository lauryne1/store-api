


from gest_store import serializers
from gest_store.models import TransactionArticle
from gest_store.models.article import Article
from gest_store.serializer.article import ArticleSerializer


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