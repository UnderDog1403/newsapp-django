from django.urls import path

from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path('',CategoryView.as_view()),
    path('<int:id>/',CategoryDetailView.as_view()),
]