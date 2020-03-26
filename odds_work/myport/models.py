from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 50)
    amount = models.CharField(max_length = 50)
    descripts = models.CharField(max_length = 120)
    

# Create your models here.
