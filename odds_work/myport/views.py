from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,viewsets
from .serializers import ItemSerializers
from .models import Item
import json

data = [{"name":"isaman","lname":"sangbamrang"}]

class ItemToList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

def my_view(request):
    return HttpResponse(json.dumps(data))

# Create your views here.
