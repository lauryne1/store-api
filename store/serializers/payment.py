from rest_framework import serializers
from store.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source="order.id", read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "order", "order_id", "payment_method", "amount", "status"]
