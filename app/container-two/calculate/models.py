from django.db import models


# Create your models here.
class Calculate(models.Model):
    file = models.CharField(max_length=500),
    product = models.CharField(max_length=500)
