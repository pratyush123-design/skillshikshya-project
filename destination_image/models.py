from django.db import models
from destination_management.models import Destination
# Create your models here.
class DestinationImage(models.Model):
  destination=models.ForeignKey(Destination,related_name='images',on_delete=models.CASCADE)
  image=models.ImageField(upload_to='destination/gallery/')
  caption=models.CharField(max_length=120,blank=True)
  created_date=models.DateTimeField(auto_now_add=True)
  updated_date=models.DateTimeField(auto_now=True) 
  def __str__(self):
   return f'{self.destination.title}-{self.caption or 'image'}'
