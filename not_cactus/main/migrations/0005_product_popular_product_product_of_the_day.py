# Generated by Django 4.1.4 on 2023-02-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_description_alter_product_full_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='Отображение на главной странице'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_of_the_day',
            field=models.BooleanField(default=False, verbose_name='Товар дня(может быть только один)'),
        ),
    ]
