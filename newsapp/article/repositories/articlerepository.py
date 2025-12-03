from django.core.paginator import Paginator

from ..models import Article
class ArticleRepository:
    def get_all(self):
        return Article.objects.filter(status = "approved").all()
    def get_by_articleslug(self, slug):
        return Article.objects.filter(slug=slug, status = "approved").first()
    def get_by_categoryslug(self,categoryslug,page=1, per_page=10):
        articles = Article.objects.filter(category__slug=categoryslug,status = "approved").order_by('updated_at')
        paginator = Paginator(articles, per_page)
        return paginator.get_page(page)
    def get_paginated_articles(self,page=1, per_page=5):
        articles = Article.objects.filter(status = "approved").all().order_by('updated_at')
        paginator = Paginator(articles, per_page)
        return paginator.get_page(page)
    def get_feature_articles(self, page =1, per_page =10):
        articles = Article.objects.filter(is_featured = True, status = "approved").order_by('updated_at')
        paginator = Paginator(articles, per_page)
        return paginator.get_page(page)

