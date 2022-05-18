from django.db import models


class Entity(models.Model):
    """Просто прокси модель для уменьшении выделения общих признаков"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
