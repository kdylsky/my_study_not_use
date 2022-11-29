from django.urls import path
from layer_study.views import create_number

urlpatterns=[
    path("", create_number)
]