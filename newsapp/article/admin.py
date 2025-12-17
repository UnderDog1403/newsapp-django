from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ('title', 'author', 'status', 'created_at')
    readonly_fields = ('author','view_count', 'slug')

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if not request.user.is_superuser:
            readonly += ['status', 'is_featured']
        return readonly

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Nếu là superuser thì xem được tất cả
        if request.user.is_superuser:
            return qs
        # Nếu không, chỉ xem được bài viết của chính mình
        return qs.filter(author=request.user)

    def has_change_permission(self, request, obj=None):
        # Nếu không có đối tượng cụ thể (ví dụ: trong danh sách), cho phép truy cập
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        if obj.status == 'approved':
            return False
        return obj.author == request.user
    def has_delete_permission(self, request, obj=None):
        # Trường hợp chưa có đối tượng cụ thể (ví dụ: trong danh sách), cho phép hiển thị nút nếu là superuser
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        return obj.author == request.user and obj.status == 'pending'


    def save_model(self, request, obj, form, change):
        if not change or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
