from django.core.paginator import Paginator

from ..models import Article
class ArticleRepository:
    def get_all(self):
        return Article.objects.all()
    def get_by_articleslug(self, slug):
        return Article.objects.filter(slug=slug).first()
    def get_by_categoryslug(self,categoryslug,page=1, per_page=10):
        articles = Article.objects.filter(category__slug=categoryslug).order_by('updated_at')
        paginator = Paginator(articles, per_page)
        return paginator.get_page(page)
    def get_paginated_articles(page=1, per_page=10):
        articles = Article.objects.all().order_by('updated_at')
        paginator = Paginator(articles, per_page)
        return paginator.get_page(page)

