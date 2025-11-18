from rest_framework_simplejwt.tokens import RefreshToken
from user.repositories.userrepository import UserRepository
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
class AuthService:
    def register_user(data):
        username = data['username']
        email =data['email']
        password =data['password']
        if UserRepository.get_by_username(username):
            raise ValueError("Tên người dùng đã tồn tại.")
        elif UserRepository.get_by_email(email):
            raise ValueError("Email đã tồn tại.")
        return UserRepository.create_user(username,email,password)

    @staticmethod
    def login(data):
        username = data["username"]
        password = data["password"]

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("Sai tên đăng nhập hoặc mật khẩu.")
        if not user.is_active:
            raise AuthenticationFailed("Tài khoản bị khóa.")
        return user

    def logout(data):
        try:
            token = RefreshToken(data)
            token.blacklist()
        except ValueError as e:
            raise ValueError("Refresh token khong hop le")

