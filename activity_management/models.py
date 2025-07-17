from django.db import models
from package_management.models import PackageManagement
# Create your models here.
class ActivityManagement(models.Model):
    name=models.CharField(max_length=200)
    package=models.ManyToManyField(PackageManagement,related_name='activities',blank=True,help_text='Packages that include this activity')
    feature_image=models.ImageField(upload_to='activity_images/',blank=True,null=True)
    description=models.TextField(blank=True)
    location=models.CharField(max_length=200,blank=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} activities are present'

