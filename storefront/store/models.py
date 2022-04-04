from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.TextField()
    text = models.TextField()
