from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, error_messages={
        "required": "Vui lòng nhập tên đăng nhập."
    })
    email = serializers.EmailField(required=True, error_messages={
        "required": "Vui lòng nhập email."
    })
    password = serializers.CharField(required=True, error_messages={
        "required": "Vui lòng nhập password."
    })
    confirm_password = serializers.CharField(required=True, error_messages={
        "required": "Vui lòng nhập confirm_password."
    })

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Mật khẩu không khớp.")
        return data



