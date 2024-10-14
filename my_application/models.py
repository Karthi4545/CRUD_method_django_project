from django.db import models

# Create your models here.
class datas(models.Model):
    name=models.CharField(max_length=50,default="")
    age=models.IntegerField(default="")
    department=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")
    