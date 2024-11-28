from rest_framework import serializers
from .models import Artisan, Product, Order


class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    artisan_name = serializers.ReadOnlyField(source="artisan.name")

    class Meta:
        model = Product
        fields = "__all__"

    def validate_inventory_count(self, value):
        if value < 0:
            raise serializers.ValidationError("Inventory count cannot be negative.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source="products", many=True, read_only=True)
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True
    )

    class Meta:
        model = Order
        fields = [
            "customer_name",
            "customer_email",
            "products",
            "product_details",
            "total_price",
        ]

    def get_product_details(self, obj):
        products = obj.products.all()
        return ProductSerializer(products, many=True).data
