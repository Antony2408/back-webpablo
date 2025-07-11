from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import AllowAny  # Permitir acceso sin autenticación

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]  # Permite acceso sin autenticación

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]  # Permite acceso sin autenticación

