import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="",upload_to="") 
    def __str__(self):
        return self.name
    
class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="",upload_to="") 
    def __str__(self):
        return self.name

class Costumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(default="",upload_to="") 
    registrated_at = models.DateTimeField("registration date")
    def __str__(self):
        return str(self.id)
    
    def sign_up_recently(self):
        return self.registrated_at >= timezone.now() - datetime.timedelta(days=1)
    

class StoreOwner(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(default="",upload_to="") 
    registrated_at = models.DateTimeField("registration date")  
    def __str__(self):
        return str(self.user)

class Store(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="",upload_to="") 
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    category = models.ForeignKey(StoreCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100) 
    picture = models.ImageField(default="",upload_to="") 
    category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default = 1)
    info = models.CharField(max_length=100000)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class MyBag(models.Model):
    costumer = models.ForeignKey(Costumer,on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    sum = 0
    for item in items:
        sum+=item.price
        
    total_price = models.PositiveIntegerField(default = sum,editable=False)
    def __str__(self):
        return str(self.id)
    

class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    sum = 0
    for item in items:
        sum+=item.price
    
    buy_time = models.DateTimeField("""PARAMETER""")
    costumer = models.ForeignKey(Costumer,on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default = sum,editable=False)