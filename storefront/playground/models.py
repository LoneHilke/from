from django.db import models
from tags import models
from store import models
# Create your models here.


class Playground(models.Model):
    title = models.TextField()
    text = models.TextField()

class Tags(models.Model):
    title = models.TextField()
    text = models.TextField()

class Store(models.Model):
    title = models.TextField()
    text = models.TextField()