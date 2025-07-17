from django.db import models

# Create your models here.


class Review(models.Model):
    STAR_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 stars

    name        = models.CharField(max_length=100)
    stars       = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    review      = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.stars} ★"
