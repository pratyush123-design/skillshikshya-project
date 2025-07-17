from django.db import models

# Create your models here.
class Query(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    message=models.TextField()
    submitted_date= models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
