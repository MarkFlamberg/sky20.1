from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
