from django.db import models
from package_management.models import PackageManagement
from destination_management.models import Destination 
# Create your models here.
class BookingManagement(models.Model):
    package=models.ForeignKey(PackageManagement,related_name='booking_management',on_delete=models.CASCADE)
    destination=models.ForeignKey(Destination,related_name='booking_management',on_delete=models.CASCADE)
    email= models.EmailField()
    phone= models.CharField(max_length=20, blank=True)
    nationality= models.CharField(max_length=100, blank=True)
    full_name= models.CharField(max_length=100)
    package_type= models.CharField(max_length=100, blank=True)  # e.g. "Standard", "Luxury"
    activity_type= models.CharField(max_length=100, blank=True)  # e.g. "Trekking", "Safari"

    activities= models.TextField(blank=True)  # Description of planned activities
    customize_trip= models.TextField(blank=True)  # Optional customization requests
    number_of_people= models.PositiveIntegerField(default=1)
    start_date= models.DateField()
    end_date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.full_name} "