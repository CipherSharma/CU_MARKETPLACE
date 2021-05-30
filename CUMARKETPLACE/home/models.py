from django.db.models import AutoField
from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    primarykey=models.AutoField(auto_created = True,primary_key = True,serialize = False,)
    sellername=models.CharField(max_length=122,null=True)
    itemname=models.CharField(max_length=122,null=True)
    address=models.CharField(max_length=300,null=True)
    description=models.TextField()
    email=models.CharField(max_length=300,null=True)
    price=models.CharField(max_length=300,null=True)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.itemname
        