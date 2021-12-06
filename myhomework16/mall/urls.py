from django.urls import path
from mall.views import shop_list, shop_detail

urlpatterns = [
    path('', shop_list),
    path('<int:pk>/', shop_detail)
]