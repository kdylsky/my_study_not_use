from django.urls import path
from orm_study.views import UserOrmView, CategoryOrmView, ProductOrmView

urlpatterns = [
    path("", UserOrmView.as_view()),
    path("1", CategoryOrmView.as_view()),
    path("2", ProductOrmView.as_view())
]