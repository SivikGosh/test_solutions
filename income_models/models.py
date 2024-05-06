from django.db import models
from polymorphic.models import PolymorphicModel


class BaseModel(PolymorphicModel):
    title = models.CharField(max_length=255)


class Storage(models.Model):

    INCOME = 'Приход'
    OUTCOME = 'Расход'

    CHOICES = [
        (INCOME, INCOME),
        (OUTCOME, OUTCOME)
    ]

    stoage_id = models.AutoField(
        verbose_name='id',
        primary_key=True
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество'
    )
    sum_cost = models.DecimalField(
        verbose_name='Сумма',
        max_digits=5,
        decimal_places=2
    )
    operation_date = models.DateField(
        verbose_name='Дата операции'
        )
    operation_type = models.CharField(
        verbose_name='Тип операции',
        max_length=255,
        choices=CHOICES
    )
    active = models.ForeignKey(
        BaseModel,
        verbose_name='Актив',
        on_delete=models.SET_NULL,
        null=True,
        related_name='storages'
    )

    def __str__(self):
        return f'{self.active}, {self.operation_date}, {self.operation_type}.'


class Magazine(BaseModel):
    magazine_id = models.AutoField(
        verbose_name='id',
        primary_key=True
    )

    def __str__(self):
        return self.title


class Newspaper(BaseModel):
    newspaper_id = models.AutoField(
        verbose_name='id',
        primary_key=True
    )

    def __str__(self):
        return self.title
