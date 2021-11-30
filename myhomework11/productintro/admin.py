from django.contrib import admin
from productintro.models import Introduce

class IntroduceAdmin(admin.ModelAdmin):
    list_display = ["product_name", "category", "created_at"]
    search_fields = ["product_name"]


admin.site.register(Introduce, IntroduceAdmin)
