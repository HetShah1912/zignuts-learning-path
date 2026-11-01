from decimal import Decimal
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse # Finds a URL using its registered Django URL name
from .models import Product

class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Keyboard",
            description="Mechanical keyboard",
            price=Decimal("1500.00"),
            stock_quantity=10,
            category="Electronics",
        )
        self.list_url = reverse("product-list")
        self.detail_url = reverse(
            "product-detail",
            args=[self.product.id],
        )

    def test_create_product(self):
        data = {
            "name": "Mouse",
            "description": "Wireless mouse",
            "price": "599.00",
            "stock_quantity": 20,
            "category": "Electronics",
        }

        response = self.client.post(
            self.list_url, data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_list_products(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_product_details(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Keyboard")

    def test_update_product(self):
        data = {
            "name": "Updated Keyboard",
            "description": "Updated description",
            "price": "1800.00",
            "stock_quantity": 15,
            "category": "Electronics",
        }

        response = self.client.put(
            self.detail_url, data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Keyboard")

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Product.objects.filter(id=self.product.id).exists()
        )

    def test_negative_price_is_rejected(self):
        data = {
            "name": "Invalid Product",
            "description": "Negative price test",
            "price": "-50.00",
            "stock_quantity": 5,
            "category": "Testing",
        }

        response = self.client.post(
            self.list_url, data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)

    def test_zero_price_is_rejected(self):
        data = {
            "name": "Free Product",
            "description": "Zero price test",
            "price": "0.00",
            "stock_quantity": 5,
            "category": "Testing",
        }

        response = self.client.post(
            self.list_url, data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)
