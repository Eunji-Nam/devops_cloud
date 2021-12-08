from django.contrib import admin

from mall.models import Cloth, Review, Tag


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
