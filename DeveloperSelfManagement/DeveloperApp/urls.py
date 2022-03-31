from django.urls import re_path
from DeveloperApp import views

urlpatterns=[
    re_path(r'^requestType$',views.RequestTypeApi),
    re_path(r'^requestType/([0-9]+)$',views.RequestTypeApi)
]