from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=225)
    email=models.TextField()
    phone=models.IntegerField()