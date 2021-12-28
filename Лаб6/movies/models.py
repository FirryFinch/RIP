from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название фильма")
    description = models.CharField(max_length=255, verbose_name="Описание фильма")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг фильма")
    is_growing = models.BooleanField(verbose_name="Увеличивается ли рейтинг фильма?")
    date_modified = models.DateTimeField(auto_now=True,
                                         verbose_name="Когда последний раз обновлялась информация о фильме?")
