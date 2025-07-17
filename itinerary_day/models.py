from django.db import models
from destination_management.models import Destination
# Create your models here.
class ItineraryDay(models.Model):
  destination=models.ForeignKey(Destination,related_name="itinerary",on_delete=models.CASCADE)
  total_days=models.PositiveSmallIntegerField()
  title=models.CharField(max_length=120)
  thumbnail=models.ImageField(upload_to="destinations/itinerary/", blank=True, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'{self.destination.title}-{self.total_days}'
  