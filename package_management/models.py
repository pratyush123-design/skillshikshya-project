from django.db import models

# Create your models here.
class PackageManagement(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    status=models.CharField(max_length=20,default='active')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    feature_image = models.ImageField(upload_to='package_images', null=True, blank=True)
   
    def __str__(self):
      return self.name 
 