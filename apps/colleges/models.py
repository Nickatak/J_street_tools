from django.db import models

# Create your models here.
class College(models.Model):
    sf_id = models.TextField()
    name = models.TextField()

