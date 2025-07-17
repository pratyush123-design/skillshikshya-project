from django.db import models
from django.utils.text import slugify
from destination_management.models import Destination
# Create your models here.
class CollectionManagement(models.Model):
   
    name=models.CharField(max_length=200,blank=True,null=True)
    slug= models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    destination=models.ForeignKey(Destination,related_name='collection',on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    def __str__(self):
     return self.name

    def save(self, *args, **kwargs):
     if not self.slug:
       self.slug = slugify(self.name)
     super().save(*args, **kwargs)     