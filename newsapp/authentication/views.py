from os import access

from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .services.authservice import AuthService
from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer =RegisterSerializer(data =request.data)
        if serializer.is_valid():
            try:
                user = AuthService.register_user(serializer.data)
                return Response({"message": "Đăng ký thành công!", "user_id": user.id}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = AuthService.login(serializer.validated_data)

            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response(
                {
                    "id": user.id,
                    "user": user.username,
                    "access": str(access),
                    "refresh": str(refresh)
                }
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh = request.data.get("refresh")
        if not refresh:
            return Response({
                "message": "Loi"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            AuthService.logout(refresh)
            return Response({"message": "Logged out successfully"}, status=205)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

