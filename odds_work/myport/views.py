from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,viewsets
from .serializers import ItemSerializers
from .models import Item
import json
##ListAPIView UpdateAPIView DestroyAPIView
data = [{"name":"isaman","lname":"sangbamrang"}]

class addItemtoList(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class updateItemtoList(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class deleteItem(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

def my_view(request):
    return HttpResponse(json.dumps(data))

# Create your views here.
