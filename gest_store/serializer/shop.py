

from gest_store import serializers
from gest_store.models.shop import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'location', 'created_at']
        read_only_fields = ['created_at']