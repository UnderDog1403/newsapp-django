from django.contrib.auth import get_user_model

User = get_user_model()
class UserRepository:
    def get_by_username(username):
        return User.objects.filter(username=username).first()
    def get_by_email(email):
        return User.objects.filter(email=email).first()
    def create_user(username,email,password):
        user =User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

