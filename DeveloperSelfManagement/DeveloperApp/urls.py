from django.urls import re_path
from DeveloperApp import views

urlpatterns=[
    re_path(r'^requestType$',views.RequestTypeApi),
    re_path(r'^requestType/([0-9]+)$',views.RequestTypeApi),
    re_path(r'^userRequest$',views.UserRequestApi),
    re_path(r'^userRequest/([0-9]+)$',views.UserRequestApi)
    
]