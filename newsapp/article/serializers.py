from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url=True)
    author = serializers.CharField(source='author.username',read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content','author','category','img']