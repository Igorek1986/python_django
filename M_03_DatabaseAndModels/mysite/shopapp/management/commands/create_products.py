from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create products")
        products_name = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]
        for product_name in products_name:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Create product {product.name}")
        # return super().handle(*args, **options)
