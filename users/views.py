from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny  # Acceso sin autenticación

class UserListView(generics.ListAPIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


