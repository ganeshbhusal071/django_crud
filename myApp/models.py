from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True,null=True)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    message=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    isdelete=models.BooleanField(default=False)
    def __str__(self):
        return self.city
