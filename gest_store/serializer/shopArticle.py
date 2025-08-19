from rest_framework import serializers
from gest_store.models.article import Article
from gest_store.models.shop import Shop
from gest_store.models.shopArticle import ShopArticle
from gest_store.serializer.article import ArticleSerializer
from gest_store.serializer.shop import ShopSerializer


class ShopArticleSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)
    shop_id = serializers.PrimaryKeyRelatedField(
        queryset=Shop.objects.all(), source='shop', write_only=True
    )
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source='article', write_only=True
    )

    class Meta:
        model = ShopArticle
        fields = ['id', 'shop', 'shop_id', 'article', 'article_id', 'stock', 'date_ajout']
        read_only_fields = ['date_ajout']