from django.urls import path

from store.views.shop import ShopDetailAPIView, ShopListCreateAPIView
from .views.store import StoreListCreateAPIView, StoreDetailAPIView

urlpatterns = [
    path("stores/", StoreListCreateAPIView.as_view(), name="store-list-create"),
    path("stores/<int:pk>/", StoreDetailAPIView.as_view(), name="store-detail"),

    # Shop endpoints
    path("shops/", ShopListCreateAPIView.as_view(), name="shop-list-create"),
    path("shops/<int:pk>/", ShopDetailAPIView.as_view(), name="shop-detail"),
]
