from django.db import models


class Womens(models.Model):

    """Создание первой модели """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_poblished = models.BooleanField(default=True)

