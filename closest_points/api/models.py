from django.db import models

# Create your models here.
class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    closest_point_x = models.IntegerField()
    closest_point_y = models.IntegerField()
