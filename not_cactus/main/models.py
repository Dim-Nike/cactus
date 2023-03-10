from django.db import models


class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/categories/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    categories = models.ForeignKey(Categories, verbose_name='Категория', on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/products/%Y/%m/%d/')
    old_price = models.IntegerField(verbose_name='Старая цена', default=0)
    price = models.IntegerField(verbose_name='Актуальная цена')
    description = models.TextField(verbose_name='Краткое описание продукта(300 символов)', default=' ', max_length=300)
    full_text = models.TextField(verbose_name='Полное описание продукта', default=' ')
    count_product = models.IntegerField(verbose_name='Остаток продукции', )
    is_active = models.BooleanField(verbose_name='Опубликовано')
    popular = models.BooleanField(verbose_name='Отображение на главной странице(может быть кратное 4)', default=False)
    product_of_the_day = models.BooleanField(verbose_name='Товар дня(может быть только один)', default=False)


class CategoriesBlog(models.Model):
    class Meta:
        verbose_name = 'Категория влога'
        verbose_name_plural = 'Категории влогов'

    name = models.CharField(verbose_name='Наименование', max_length=155)
    image = models.ImageField(verbose_name='Фотография', upload_to='photo/CategoriesBlog/%Y/%m/%d/')


    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        verbose_name = 'Влог'
        verbose_name_plural = 'Влоги'

    name = models.CharField(verbose_name='Название темы', max_length=155)
    categories = models.ForeignKey(CategoriesBlog, verbose_name='Категория', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Фотография', upload_to='photo/blog/%Y/%m/%d/')
    description = models.CharField(verbose_name='Подзаголовок(300 символов)', max_length=300)
    full_text = models.TextField(verbose_name='Текст влога')
    is_active = models.BooleanField(verbose_name='Опубликовано')
    popular = models.BooleanField(verbose_name='Популярный влог', default=False)
    create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)



