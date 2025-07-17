from django.db import models
from destination_management.models import Destination
# Create your models here.
class CostItem(models.Model):
    destination=models.ForeignKey(Destination,related_name='costs',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    label=models.CharField(max_length=100)
    currency=models.CharField(max_length=10, default="USD")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.label}: {self.amount}-{self.currency}"