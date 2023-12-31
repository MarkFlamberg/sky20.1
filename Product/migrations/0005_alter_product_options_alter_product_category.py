# Generated by Django 4.2.5 on 2023-10-04 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0002_alter_category_options'),
        ('Product', '0004_remove_product_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category', verbose_name='Категория'),
        ),
    ]
