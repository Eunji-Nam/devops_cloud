from django.contrib import admin

from mall.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at"]
    list_display_links = ["name"]

admin.site.register(Shop, ShopAdmin)
