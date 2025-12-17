from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User  # hoặc từ đường dẫn đúng tới model

admin.site.register(User)