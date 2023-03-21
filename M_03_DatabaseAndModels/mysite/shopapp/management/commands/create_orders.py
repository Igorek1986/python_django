from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create orders")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Russia, Tjumen, Respublici, 999",
            promocode="DJANGO",
            user=user,
        )
        self.stdout.write(f"Created order {order}")
        order = Order.objects.first()
        if not order:
            self.stdout.write("No Order yet")
            return
        else:
            products = Product.objects.all()
            for product in products:
                order.products.add(product)
            order.save()
            self.stdout.write(
                f"Successfuly add products {order.products.all()} for orders {order}"
            )
        # return super().handle(*args, **options)
