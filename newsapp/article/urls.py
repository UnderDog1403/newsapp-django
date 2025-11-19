from .views import ArticleListView, ArticleByCategoryView
from django.urls import path
urlpatterns = [
    path('',ArticleListView.as_view()),
    path('/category/<slug:category_slug>/',ArticleByCategoryView.as_view()),
]