from django.urls import path

from store.views.cart import CartDetailAPIView, CartListCreateAPIView
from store.views.cart_item import CartItemDetailAPIView, CartItemListCreateAPIView
from store.views.category import CategoryDetailAPIView, CategoryListCreateAPIView
from store.views.order import OrderDetailAPIView, OrderListCreateAPIView
from store.views.order_item import OrderItemDetailAPIView, OrderItemListCreateAPIView
from store.views.payment import PaymentDetailAPIView, PaymentListCreateAPIView
from store.views.products import ProductDetailAPIView, ProductListCreateAPIView
from store.views.shop import ShopDetailAPIView, ShopListCreateAPIView
from .views.store import StoreListCreateAPIView, StoreDetailAPIView

urlpatterns = [
    path("stores/", StoreListCreateAPIView.as_view(), name="store-list-create"),
    path("stores/<int:pk>/", StoreDetailAPIView.as_view(), name="store-detail"),

    # Shop endpoints
    path("shops/", ShopListCreateAPIView.as_view(), name="shop-list-create"),
    path("shops/<int:pk>/", ShopDetailAPIView.as_view(), name="shop-detail"),

     # Category endpoints
    path("categories/", CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),

     # Cart endpoints
    path("carts/", CartListCreateAPIView.as_view(), name="cart-list-create"),
    path("carts/<int:pk>/", CartDetailAPIView.as_view(), name="cart-detail"),

     # CartItem
    path("cart-items/", CartItemListCreateAPIView.as_view(), name="cartitem-list-create"),
    path("cart-items/<int:pk>/", CartItemDetailAPIView.as_view(), name="cartitem-detail"),

    # OrderItem
    path("order-items/", OrderItemListCreateAPIView.as_view(), name="orderitem-list-create"),
    path("order-items/<int:pk>/", OrderItemDetailAPIView.as_view(), name="orderitem-detail"),

    # Orders
    path("orders/", OrderListCreateAPIView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),

     # Products
    path("products/", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),

       # Payments
    path("payments/", PaymentListCreateAPIView.as_view(), name="payment-list-create"),
    path("payments/<int:pk>/", PaymentDetailAPIView.as_view(), name="payment-detail"),
]
