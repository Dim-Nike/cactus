# Generated by Django 4.1.4 on 2023-02-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=' ', verbose_name='Краткое описание продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='full_text',
            field=models.TextField(default=' ', verbose_name='Полное описание продукта'),
        ),
    ]
