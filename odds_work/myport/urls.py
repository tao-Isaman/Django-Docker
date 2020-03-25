from django.urls import path , include
from django.conf.urls import url
from .views import *




urlpatterns = [
    url(r'^$',my_view),
]