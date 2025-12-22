from django.db import models
from django.db.models import ForeignKey

from django.conf import settings


# Create your models here.
class SaveArticle(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='savearticles'
    )
    article = models.ForeignKey(
        'article.Article',
        on_delete=models.CASCADE,
        related_name='savearticles'
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'article'], name='unique_user_article')
        ]

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.article.title}"
