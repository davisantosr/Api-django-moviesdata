from django.db import models

# Create your models here.

class Moviedata(models.Model):
  name = models.CharField(max_length=100)
  duration = models.FloatField()
  rating = models.FloatField()
  typ = models.CharField(max_length=100, default='action')

  def __str__(self):
    return self.name
