from django.db import models


class MainPageContent(models.Model):
    phone_number = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.CharField(max_length=120)

    def __str__(self):
        return f"ID: {self.id} | Phone: {self.phone_number}"

    class Meta:
        verbose_name = ("Главный-баннер")
        verbose_name_plural = ("Главный-баннер")


# TODO: is_published=True
class BannerImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()
    image = models.ImageField(upload_to="banners/")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"ID: {self.id} | Order: {self.order}"

    class Meta:
        verbose_name = ("Баннер-фото")
        verbose_name_plural = ("Баннер-фото")


# TODO: 3 ta
class MainPageCard(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150)
    image = models.ImageField(upload_to="main_page_cards/")

    def __str__(self):
        return f"ID: {self.id} | TITLE: {self.title}"

    class Meta:
        verbose_name = ("Баннер")
        verbose_name_plural = ("Баннеры")

# TODO: 3 ta
class MainPageServiceCard(models.Model):
    icon = models.ImageField(upload_to="main_page_service_cards/")
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150)

    def __str__(self):
        return f"ID: {self.id} | TITLE: {self.title}"

    class Meta:
        verbose_name = ("Баннеры-карты")
        verbose_name_plural = ("Баннеры")