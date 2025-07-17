from django.db import models

# Create your models here.
class HomePage(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    video_file=models.FileField(upload_to="homepage/videos/", blank=True, null=True)
    video_link=models.URLField(blank=True,null=True,help_text="eg: YouTube/Vimeo URL")
    preview=models.ImageField(upload_to="homepage/video_preview",blank=True,null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.title or "Homepage Video"
    

