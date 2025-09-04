from rest_framework import serializers
from store.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "user_name", "total_amount", "status", "created_at"]
