from django.contrib import admin

from mall.models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price"]
    list_display_links = ["name"]

