from django.db import models
from destination_management.models import Destination
# Create your models here.
class GearItem(models.Model):
    destination=models.ForeignKey(Destination,related_name='gear_items',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True)
    required=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return f"{self.destination.title}-{self.name}"
    