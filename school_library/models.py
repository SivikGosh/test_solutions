from django.db import models
from income_models.models import BaseModel


class Author(models.Model):
    author_id = models.AutoField(
        verbose_name='id',
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=255
    )

    def __str__(self):
        return self.name


class Book(BaseModel):
    book_id = models.AutoField(
        verbose_name='id',
        primary_key=True
    )
    is_active = models.BooleanField()
    author = models.ForeignKey(
        Author,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title
