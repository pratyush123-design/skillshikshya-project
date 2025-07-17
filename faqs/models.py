from django.db import models
from destination_management.models import Destination
# Create your models here.
class FAQs(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    destination=models.ForeignKey(Destination,on_delete=models.CASCADE,related_name='faqs')
    def __str__(self):
        return self.title
    