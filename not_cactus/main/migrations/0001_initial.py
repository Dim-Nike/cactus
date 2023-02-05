# Generated by Django 4.1.4 on 2023-02-05 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Наименование')),
                ('photo', models.ImageField(upload_to='photo/categories/%Y/%m/%d/', verbose_name='Фотография')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Наименование')),
                ('photo', models.ImageField(upload_to='photo/products/%Y/%m/%d/', verbose_name='Фотография')),
                ('old_price', models.IntegerField(default=0, verbose_name='Старая цена')),
                ('price', models.IntegerField(verbose_name='Актуальная цена')),
                ('count_product', models.IntegerField(verbose_name='Остаток продукции')),
                ('is_active', models.BooleanField(verbose_name='Опубликовано')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categories', verbose_name='Категория')),
            ],
        ),
    ]
