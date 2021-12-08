from django.urls import path
from mall import views

app_name = 'mall'

urlpatterns = [
        # path(루트(주소))를 만들어 줌, 링크를 클릭했을 때 호출 할 뷰함수, url reverse때 이용하는 이름)
    path('', views.cloth_list, name="cloth_list"),
    path('<int:pk>/', views.cloth_detail, name="cloth_detail"),
    path('tags/<str:tag_category>', views.tag_detail, name="tag_detail"),
]