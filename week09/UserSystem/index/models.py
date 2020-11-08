from django.db import models

# Create your models here.
class PersonList(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30,unique=True, blank=False)
    Password = models.CharField(max_length=30)