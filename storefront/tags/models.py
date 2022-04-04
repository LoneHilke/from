from django.db import models

# Create your models here.
class Tags(models.Model):
    title = models.TextField()
    text = models.TextField()