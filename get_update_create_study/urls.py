from django.urls import path
from get_update_create_study.views import StudentView, StudentTwoView

urlpatterns=[
    path("", StudentView.as_view()),
    path("1", StudentTwoView.as_view())
]