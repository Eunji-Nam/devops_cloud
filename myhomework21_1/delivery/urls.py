from django.urls import path
from delivery import views

app_name = "delivery"

urlpatterns = [
    path("", views.shop_list, name="shop_list")
]