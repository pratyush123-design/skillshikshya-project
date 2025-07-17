from django.db import models
from django.utils.text import slugify
# Create your models here.
class BLog(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,null=True,blank=True)
    reading_time=models.CharField(max_length=200,help_text='eg:5 minutes',null=True,blank=True)
    description=models.TextField()
    feature_image=models.ImageField(upload_to="blogs/feature/", blank=True, null=True)
    is_popular=models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    def __str__(self):
     return self.title

    def save(self, *args, **kwargs):
     if not self.slug:
       self.slug = slugify(self.name)
     super().save(*args, **kwargs)     
