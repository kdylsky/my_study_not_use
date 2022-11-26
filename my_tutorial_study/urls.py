from django.urls import path
from my_tutorial_study.views import book_get_post, book_detail

urlpatterns = [
    path('book/', book_get_post),
    path('book/<int:pk>/', book_detail),
]