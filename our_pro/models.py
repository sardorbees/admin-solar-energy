from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='works/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    completed_at = models.DateField()

    def __str__(self):
        return self.title
