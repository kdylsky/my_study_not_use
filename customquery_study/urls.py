from django.urls import path

from customquery_study.views import account_create

urlpatterns =[
    path("queryset", account_create)
]