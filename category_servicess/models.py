from django.db import models
from django.urls import reverse

# Create your models here.
class CategoryTitle(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug =  models.CharField(max_length=100, unique=True)

    def get_url(self):
        return reverse('products_category', args=[self.slug])

    def __str__(self):
        return self.category_name
    


    class Meta:
        verbose_name = 'Товарная катерогия'
        verbose_name_plural = 'Товарная катерогия'
    


