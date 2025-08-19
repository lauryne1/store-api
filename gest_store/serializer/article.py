

from gest_store import serializers
from gest_store.models.article import Article
from gest_store.models.categorie import Categorie
from gest_store.serializer.categorie import CategorieSerializer


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorieSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Article
        fields = ['id', 'name', 'price', 'stock', 'opened_at', 'category', 'category_id']
        read_only_fields = ['opened_at']