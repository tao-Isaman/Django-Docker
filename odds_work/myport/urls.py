from django.urls import path , include
from django.conf.urls import url
from .views import *




urlpatterns = [
    url(r'^$',my_view),
    url(r'^addItem$',addItemtoList.as_view()),
    url(r'^updateItem/(?P<pk>\d+)$',updateItemtoList.as_view()),
    url(r'^deleteItem/(?P<pk>\d+)$',deleteItem.as_view()),
    url(r'^itemList$',ItemList.as_view()),
]