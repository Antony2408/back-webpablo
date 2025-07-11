from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
# Importa las clases de permisos de Django Rest Framework (solo si quieres usarlas)
# from rest_framework.permissions import IsAuthenticated

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # comment or remove the following line to allow public access without authentication
    # permission_classes = [IsAuthenticated]  # Esto es lo que bloquea el acceso sin token

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # comment or remove the following line to allow public access without authentication
    # permission_classes = [IsAuthenticated]  # Esto es lo que bloquea el acceso sin token
