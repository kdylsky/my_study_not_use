from django.urls import path
from my_tutorial_study.views import BookAPI, BookDetailAPI, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('book/', BookAPI.as_view()),
    path('book/<int:pk>/', BookDetailAPI.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
