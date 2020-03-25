from django.shortcuts import render
from django.http import HttpResponse
import json

data = [{"name":"isaman","lname":"sangbamrang"}]

def my_view(request):
    return HttpResponse(json.dumps(data))

# Create your views here.
