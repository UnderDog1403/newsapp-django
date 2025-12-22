# factories.py
import factory
from faker import Faker
from .models import Category
from django.utils.text import slugify
fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")  # sinh tên ngẫu nhiên
    slug = factory.LazyAttribute(lambda o: slugify(o.name))  # tự tạo slug từ name