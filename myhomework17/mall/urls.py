from django.urls import path
from mall import views

app_name = 'mall'

urlpatterns = [
    path('', views.cloth_list, name="cloth_list"),
    path('<int:pk>/', views.cloth_detail, name="cloth_detail"),
    path('tags/<str:tag_category>', views.tag_detail, name="tag_detail"),
]