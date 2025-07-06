from django.contrib import admin

from base.models import *


@admin.register(MainPageContent)
class MainPageContentAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "email", "address")
    list_display_links = ("phone_number",)


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "order", "is_published")
    list_display_links = ("created_at", )
    list_editable = ("is_published", )


@admin.register(MainPageCard)
class MainPageCardAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title", )


@admin.register(MainPageServiceCard)
class MainPageServiceCardAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title",)

