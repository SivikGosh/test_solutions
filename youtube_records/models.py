from django.db import models


class Record(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    def __str__(self):
        return self.title
