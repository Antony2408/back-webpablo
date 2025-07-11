# users/urls.py
from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView, UserListView  
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta para login con JWT
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token
    path('register/', RegisterView.as_view(), name='register'),  # Ruta para registrar un nuevo usuario
    path('users/', UserListView.as_view(), name='user_list'),  # Acceso público a los usuarios
]
