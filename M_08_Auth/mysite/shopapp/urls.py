from django.urls import path

from .views import (
    shop_index,
    groups_list,
    ProductListView,
    ProductDetailView,
    ProductCreatView,
    ProductUpdateView,
    ProductArchivedView,
    OrderListView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
    OrderCreateView,
)

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/create/", ProductCreatView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/archived/",
        ProductArchivedView.as_view(),
        name="product_archived",
    ),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete", OrderDeleteView.as_view(), name="order_delete"),
]
