from django.db import models
from django.urls import reverse

# Create your models here.
class Category_Title_Text(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug =  models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category_title_text'
        verbose_name_plural = 'category_title_text'

    def get_url(self):
        return reverse('products_category', args=[self.slug])

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Катерогия_техта-мини'
        verbose_name_plural = 'Катерогия_техта-мини'
