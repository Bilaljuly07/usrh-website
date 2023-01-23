from django.db import models

# Create your models here.

class Sponsors(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')
    link = models.TextField()
    types = models.CharField(max_length=150)

    def __str__(self):
        return self.name