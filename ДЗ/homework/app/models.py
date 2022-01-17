from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=200)
    site = models.CharField(max_length=200)


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название фильма")
    description = models.CharField(max_length=255, verbose_name="Описание фильма")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг фильма")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)



