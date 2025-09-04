from rest_framework import serializers
from store.models.cart_item import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "product_name", "quantity_in_stock"]
