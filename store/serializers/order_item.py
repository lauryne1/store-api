from rest_framework import serializers
from store.models.order_item import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "product_name", "quantity_in_stock", "price"]
