

from gest_store import serializers
from gest_store.models.categorie import Categorie


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name', 'description']