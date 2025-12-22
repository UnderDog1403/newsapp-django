from django.urls import path
from .views import SaveArticleView
urlpatterns = [
    path('',SaveArticleView.as_view()),


]