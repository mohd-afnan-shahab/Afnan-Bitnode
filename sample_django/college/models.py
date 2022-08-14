from django.db import models


class College(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    email =  models.EmailField(max_length=200) 
