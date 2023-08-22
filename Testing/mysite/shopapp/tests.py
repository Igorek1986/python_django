from django.test import TestCase
from django.contrib.auth.models import Permission, User
from django.urls import reverse
from .models import Order


class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username="alex", password="qwerty")
        permission_view_order = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(permission_view_order)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address="test street",
            promocode="test",
            user=self.user,
        )

    def tearDown(self) -> None:
        self.order.delete()

    def test_order_details(self):
        response = self.client.get(
            reverse(
                "shopapp:order_details",
                kwargs={"pk": self.order.pk},
            ),
        )
        received_data = response.context["order"].pk
        expected_data = self.order.pk

        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(received_data, expected_data)


class OrdersExportTestCase(TestCase):
    fixtures = [
        "users-fixtures.json",
        "products-fixture.json",
        "orders-fixture.json",
    ]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username="alex", password="qwerty")
        cls.user.is_staff = True
        cls.user.save()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_export(self):
        response = self.client.get(reverse("shopapp:orders-export"))
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user_id": order.user_id,
                "product_id": [product.id for product in order.products.all()],
            }
            for order in orders
        ]
        order_data = response.json()
        self.assertEqual(order_data["orders"], expected_data)
