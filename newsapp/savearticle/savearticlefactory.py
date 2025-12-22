# savearticle/factories.py
import factory
from .models import SaveArticle
from article.articlefactory import ArticleFactory
from user.userfactory import UserFactory   # giả sử bạn để UserFactory trong app users

class SaveArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SaveArticle

    user = factory.SubFactory(UserFactory)         # liên kết với user giả
    article = factory.SubFactory(ArticleFactory)

