from django.db import models
from django.urls import reverse


class Currency(models.TextChoices):
    USD = 'usd', 'Доллар США'
    EUR = 'eur', 'Евро'
    GBP = 'gbp', 'Фунт стерлингов'
    JPY = 'jpy', 'Японская иена'
    AUD = 'aud', 'Австралийский доллар'
    CAD = 'cad', 'Канадский доллар'


class Item(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена', default=0)
    currency = models.CharField(max_length=3, choices=Currency.choices, default='usd')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
