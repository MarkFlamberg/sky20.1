from django.db import models

from Category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='Product/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    data_creation = models.DateField(null=True, blank=True, verbose_name='Дата создания')
    data_change = models.DateTimeField(null=True, blank=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'


