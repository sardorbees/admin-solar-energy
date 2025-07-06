from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField('Категория техта',max_length=255, unique=True)
    slug = models.SlugField('Категория url', max_length=255, unique=True, blank=True)
    image = models.ImageField('Категория фото',upload_to='categories/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Категория карточка'
        verbose_name_plural = 'Категория карточка'
