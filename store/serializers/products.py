from rest_framework import serializers
from store.models.products import Product

class ProductSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source="shop.name", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "quantity_in_stock", "shop", "shop_name"]
