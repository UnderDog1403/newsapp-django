from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from .services.articleservice import ArticleService
# Create your views here.

class ArticleListView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ArticleService()
    def get(self, request):
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 5))
        try:
            articles = self.service.get_articles_paginated(page, per_page)
            serialized = ArticleSerializer(articles, many=True)
            # if serialized.is_valid():
            return Response({
                'data': serialized.data,
                'count': articles.paginator.count,
                'num_pages': articles.paginator.num_pages,
                'current_page': articles.number
            })
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
class ArticleByCategoryView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ArticleService()
    def get(self, request, category_slug):
        page = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 10)
        try:
            articles = self.service.get_article_paginated_by_categoryslug(category_slug, page, per_page)
            serialized = ArticleSerializer(articles, many=True)
            return Response({
                'results': serialized.data,
                'count': articles.paginator.count,
                'num_pages': articles.paginator.num_pages,
                'current_page': articles.number
            })
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

class ArticleFeaturedView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ArticleService()
    def get(self, request, ):
        page = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 10)
        try:
            articles = self.service.get_articles_paginated_featured(page,per_page)
            serialized = ArticleSerializer(articles,many=True)
            return Response({
                'results': serialized.data,
                'count': articles.paginator.count,
                'num_pages': articles.paginator.num_pages,
                'current_page': articles.number
            })
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
class ArticleDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ArticleService()
    def get(self,request,slug):
        try:
            article = self.service.get_by_slug(slug)
            serialized = ArticleSerializer(article)
            return Response({
                'results': serialized.data,
            })
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


