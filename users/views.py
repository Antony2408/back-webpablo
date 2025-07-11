# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Personalizar el Token para incluir datos adicionales
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Puedes agregar más información al token si lo necesitas
        token["username"] = user.username
        token["email"] = user.email
        # Por ejemplo, puedes agregar el rol del usuario si tienes ese campo
        token["role"] = user.role  
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Agregar datos completos del usuario en la respuesta
        data["user"] = {
            "username": self.user.username,
            "email": self.user.email,
            "role": self.user.role,
        }
        return data

# Crear la vista personalizada del token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


