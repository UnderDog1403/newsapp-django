from .views import ArticleListView, ArticleByCategoryView, ArticleFeaturedView, ArticleDetailView
from django.urls import path
urlpatterns = [
    path('',ArticleListView.as_view()),
    path('category/<slug:category_slug>/',ArticleByCategoryView.as_view()),
    path('featured',ArticleFeaturedView.as_view()),
    path('<slug:slug>',ArticleDetailView.as_view()),
]