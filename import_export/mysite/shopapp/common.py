from csv import DictReader
from io import TextIOWrapper

from shopapp.models import Order


def save_csv_orders(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    orders = [Order(**row) for row in reader]
    for order in orders:
        parameters = {
            "delivery_address": order.delivery_address,
            "promocode": order.promocode,
            "user": order.user,
        }
        _order = Order.objects.create(**parameters)
        print(order.id)
        for pr_id in order.id.split(" "):
            _order.products.add(pr_id)

    return orders
