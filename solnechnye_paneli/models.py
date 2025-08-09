# products/models.py
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name=("таг"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категория")

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    slug = models.SlugField(unique=True, verbose_name=("товар url"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=("категория"))
    description = models.TextField(verbose_name=("описание"))
    image = models.ImageField(upload_to='products/', verbose_name=("изображение"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=("цена"))
    old_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=("старая_цена"))
    color = models.CharField(max_length=50, verbose_name=("цвет"))
    tag = models.CharField(max_length=100, null=True, blank=True, verbose_name=("ярлык"))
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name=("рейтинг"))
    reviews = models.IntegerField(default=0, verbose_name=("обзоры"))
    in_stock = models.BooleanField(default=True, verbose_name=("в наличии"))
    installment_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=("рассрочка_цена"))
    is_available = models.BooleanField(default=True, verbose_name=("астивна"))
    views = models.IntegerField(default=0, verbose_name=("просмотров"))
    popularity = models.IntegerField(default=0, verbose_name=("популярность"))
    power = models.PositiveIntegerField(null=True, blank=True, verbose_name=("w сколько"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ("Товар")

from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=100, verbose_name=("имя"))
    slug = models.SlugField(unique=True, verbose_name=("товар url"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("w сколько")
        verbose_name_plural = ("w сколько")

from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    slug = models.SlugField(unique=True, verbose_name=("товар url"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Товар описание")
        verbose_name_plural = ("Товар описание")

# shop_category/models.py

from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=("имя"))
    slug = models.SlugField(unique=True, blank=True, verbose_name=("url товар"))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=("цена"))
    rating = models.FloatField(default=0, verbose_name=("райтинг"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Бранд")
        verbose_name_plural = ("Бранд")

from django.db import models


class SolarPanel(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    power = models.IntegerField(verbose_name=("w сколько"))  # мощность в ваттах
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("цена"))
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=("старая цена"))
    image = models.ImageField(upload_to='panels/', verbose_name=("фото"))

    def __str__(self):
        return f"{self.name} - {self.power}W"

    class Meta:
        verbose_name = ("Солнечная панель доп")
        verbose_name_plural = ("Солнечная панель доп")