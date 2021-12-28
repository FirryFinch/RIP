from django.db import models


# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=30)
    site = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'platforms'


class Movie(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    platform = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'movies'
