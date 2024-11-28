from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Artisan, Product, Order
from .serializers import ArtisanSerializer, ProductSerializer, OrderSerializer


class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = Artisan.objects.all()
    serializer_class = ArtisanSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]
    ordering = ["-created_at"]

    @action(detail=False, methods=["get"])
    def recommendations(self, request):
        recommended_products = Product.get_recommended_products()
        serializer = self.get_serializer(recommended_products, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        order = Order.objects.create(
            customer_name=data["customer_name"], customer_email=data["customer_email"]
        )
        for id in data["products"]:
            order.products.add(id)
            order.save()
        return Response({"message": "order saved"}, status=status.HTTP_201_CREATED)
