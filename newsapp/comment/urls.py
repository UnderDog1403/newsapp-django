from django.urls import path

from .views import CommentView, CommentDetailView, CommentByArticleView

urlpatterns = [
    path('',CommentView.as_view()),
    path('<int:id>',CommentDetailView.as_view()),
    path('article/<slug:article_slug>/', CommentByArticleView.as_view()),

]