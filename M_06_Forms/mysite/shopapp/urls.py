from django.urls import path

from .views import (
    shop_index,
    groups_list,
    products_list,
    products_create,
    orders_list,
    orders_create,
)

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", products_list, name="products_list"),
    path("products/create/", products_create, name="product_create"),
    path("orders/", orders_list, name="orders_list"),
    path("orders/create/", orders_create, name="orders_create"),
]
