from django.db import models
from django.db.models import Count


class Artisan(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.PositiveIntegerField()
    artisan = models.ForeignKey(
        Artisan, on_delete=models.CASCADE, related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_recommended_products(cls):
        """Returns the top 5 most ordered products."""
        return cls.objects.annotate(order_count=Count("order")).order_by(
            "-order_count"
        )[:5]


class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk and self.products.exists():
            total = sum(product.price for product in self.products.all())
            if self.total_price != total:
                self.total_price = total
                super().save(update_fields=["total_price"])

        for product in self.products.all():
            if product.inventory_count > 0:
                product.inventory_count -= 1
                product.save()
            else:
                raise ValueError(f"Product '{product.name}' is out of stock!")

    def __str__(self):
        return f"Order by {self.customer_name}"
