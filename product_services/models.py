from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title