from django.urls import path
from my_tutorial_study.views import BookAPI

urlpatterns = [
    path('book/', BookAPI.as_view()),
    # path('book/<int:pk>/', DetailBookAPI.as_view()),
]