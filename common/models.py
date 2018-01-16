from django.db import models

# Create your models here.
class key(models.Model):
  key = models.CharField(max_length=50)
  number = models.BigIntegerField(default=0)