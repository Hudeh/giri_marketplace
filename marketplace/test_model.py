from rest_framework.test import APITestCase
from rest_framework import status
from .models import Artisan, Product, Order


class ArtisanAPITestCase(APITestCase):
    def setUp(self):
        self.artisan = Artisan.objects.create(
            name="Henry Udeh",
            email="henry@gmail.com",
            phone="admin12345",
            location="New York",
        )

    def test_create_artisan(self):
        data = {
            "name": "Jane Smith",
            "email": "jane@gmail.com",
            "phone": "9876543210",
            "location": "Los Angeles",
        }
        response = self.client.post("/api/artisans/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artisan.objects.count(), 2)

    def test_get_artisan_list(self):
        response = self.client.get("/api/artisans/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.artisan = Artisan.objects.create(
            name="Henry Udeh",
            email="henry@gmail.com",
            phone="admin12345",
            location="New York",
        )
        self.product = Product.objects.create(
            name="Handmade Vase",
            description="A beautiful handmade vase.",
            price=50.00,
            inventory_count=1000,
            artisan=self.artisan,
        )

    def test_create_product(self):
        data = {
            "name": "Wooden Bowl",
            "description": "A bowl made of wood.",
            "price": 30.00,
            "inventory_count": 150,
            "artisan": self.artisan.id,
        }
        response = self.client.post("/api/products/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_get_product_recommendations(self):
        # Simulate orders to increase popularity
        order = Order.objects.create(
            customer_name="Alice",
            customer_email="alice@gmail.com",
        )
        order.products.add(self.product)

        response = self.client.get("/api/products/recommendations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.artisan = Artisan.objects.create(
            name="Henry Udeh",
            email="henry@gmail.com",
            phone="admin12345",
            location="New York",
        )
        self.product = Product.objects.create(
            name="Handmade Vase",
            description="A beautiful handmade vase.",
            price=50.00,
            inventory_count=100,
            artisan=self.artisan,
        )

    def test_create_order(self):
        data = {
            "products": [self.product.id],
            "customer_name": "Alice",
            "customer_email": "alice@gmail.com",
        }
        response = self.client.post("/api/orders/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.product.refresh_from_db()
        self.assertEqual(self.product.inventory_count, 99)

    def test_out_of_stock_error(self):
        self.product.inventory_count = 0
        self.product.save()
        data = {
            "products": [self.product.id],
            "customer_name": "Alice",
            "customer_email": "alice@gmail.com",
        }
        response = self.client.post("/api/orders/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
