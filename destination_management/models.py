from django.db import models
from django.utils.text import slugify
from activity_management.models import ActivityManagement
# Create your models here.
class Destination(models.Model):
  activity = models.ForeignKey(
    "activity_management.ActivityManagement",
    on_delete=models.SET_NULL,
    null=True,
    blank=True)
  title=models.CharField(max_length=100,null=True,blank=True)
  slug=models.SlugField(max_length=100,null=True,blank=True)
  best_season=models.CharField(max_length=40,blank=True)
  difficulty=models.CharField(max_length=20,null=True,blank=True)   #eg moderate,easy, etc
  meals=models.CharField(max_length=200,null=True,blank=True)
  group_size=models.CharField(max_length=200,null=True,blank=True)
  trip_nature=models.CharField(max_length=100,null=True,blank=True)
  accomodation=models.CharField(max_length=100,null=True,blank=True)
  max_altitude=models.CharField(max_length=100,null=True,blank=True)
  created_date= models.DateTimeField(auto_now_add=True)
  updated_date= models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if not self.slug:
       self.slug = slugify(self.name)
    super().save(*args, **kwargs)     