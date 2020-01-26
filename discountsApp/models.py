from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Product(models.Model):

    Product_ID = models.AutoField(primary_key=True) 
    ProductName = models.CharField(max_length=200) #product name

    PubTime = models.DateTimeField(auto_now=False, auto_now_add=False) 
    EndTime = models.DateTimeField(auto_now=False, auto_now_add=False) 

    OriPrice = models.FloatField(default=0)
    DisPrice = models.FloatField(default=0)

    Shoplink = models.URLField(max_length=500)
    imglink = models.URLField(max_length=500)

    Tag = models.CharField(max_length=200)
    click = models.IntegerField(default=0)
    

    def __str__(self):
        return self.ProductName
    
    def isExpired(self):
        now = timezone.now()
        if self.EndTime >now:
            return False
        else:
            return True

    isExpired.admin_order_field = 'PubTime'

    def showEndTime(self):
        return self.EndTime.strftime('%D')
