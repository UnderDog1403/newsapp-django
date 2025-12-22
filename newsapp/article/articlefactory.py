import factory
from django.contrib.auth import get_user_model
from faker import Faker
from category.categoryfactory import CategoryFactory
from user.userfactory import UserFactory
from .models import Article

fake = Faker()
User = get_user_model()

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker("sentence", nb_words=6)
    slug = factory.LazyAttribute(lambda o: fake.slug())
    # img có thể bỏ qua hoặc dùng SimpleUploadedFile nếu muốn test upload
    img = None
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    status = factory.Iterator(["pending", "approved", "hidden"])
    is_featured = factory.Faker("boolean")
    view_count = factory.Faker("random_int", min=0, max=1000)
    content = factory.Faker("text", max_nb_chars=500)