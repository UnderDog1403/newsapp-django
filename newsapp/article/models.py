from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from tinymce.models import HTMLField
from django.utils.text import slugify
from PIL import Image, ImageOps

class Article(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('hidden', 'Ẩn'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    img = models.ImageField(upload_to='articles/', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    category = models.ForeignKey(
        'category.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    is_featured = models.BooleanField(default=False)

    view_count = models.PositiveIntegerField(default=0)

    content = HTMLField()  # lưu rich text từ TinyMCE

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Tự tạo slug nếu không nhập
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)  # lưu tạm để có file path

        if self.img:
            img_path = self.img.path
            img = Image.open(img_path)
            # Resize về đúng kích thước
            img = ImageOps.fit(img, (150, 200), Image.Resampling.LANCZOS)
            img.save(img_path)

    def __str__(self):
        return self.title