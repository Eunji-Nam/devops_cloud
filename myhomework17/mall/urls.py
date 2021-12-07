from django.urls import path
from mall import views

app_name = 'mall'

urlpatterns = [
    path('', views.cloth_list, name="cloth_list"),
]