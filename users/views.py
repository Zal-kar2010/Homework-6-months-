from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, CustomTokenObtainPairSerializer

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class AuthorizationAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user:
            return Response({"message": "Успешный вход"})
        return Response({"error": "Неверный email или пароль"}, status=status.HTTP_400_BAD_REQUEST)

class ConfirmUserAPIView(generics.GenericAPIView):
    def get(self, request):
        return Response({"message": "Подтверждение пользователя"})

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
