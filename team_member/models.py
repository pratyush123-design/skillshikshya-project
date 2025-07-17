from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to="team/")
    show_on_homepage=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return f'{self.name} - {self.position}'