from django.db import models
from destination_management.models import Destination
# Create your models here.
class Departure(models.Model):
       STATUS_CHOICES = (
        ("guaranteed", "Guaranteed"),
        ("limited", "Limited"),
        ("full", "Full"),
    )
       destination=models.ForeignKey(Destination,related_name='departures',on_delete=models.CASCADE)
       start_date=models.DateField()
       end_date=models.DateField()
       price=models.DecimalField(max_digits=10,decimal_places=3)
       currency=models.DecimalField(max_digits=10,decimal_places=2)
       status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="guaranteed")
       def __str__ (self):
              return f"{self.destination.title}: {self.start_date} → {self.end_date} (${self.price} {self.currency})"
       