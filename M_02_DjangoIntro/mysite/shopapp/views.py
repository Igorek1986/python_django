from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def shop_index(request: HttpRequest):
    products = [
        ("Apple watch", 300),
        ("iPhone", 999),
        ("iMac", 3999),
    ]
    context = {"products": products}

    return render(request, "shopapp/shop-index.html", context=context)
