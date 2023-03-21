from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    atchived = models.BooleanField(default=False)


class Order(models.Model):
    delivery_address = models.TextField(blank=True)
    promocode = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
