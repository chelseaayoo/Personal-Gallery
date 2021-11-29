from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

  
    def __str__(self):
        return self.name
    
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)  
    description = models.TextField()

    @classmethod
    def search_by_title(cls,seearch_term):
        return Image