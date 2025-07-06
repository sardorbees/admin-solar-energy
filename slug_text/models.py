from django.db import models
from django.urls import reverse
class SlugCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)


    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'