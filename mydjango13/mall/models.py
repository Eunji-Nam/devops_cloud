import datetime
from django.db import models


class Shop(models.Model):
    # id = models.BigAutoField(primary_key=True)
    # -- 장고에서는 id를 데이터에 대한 address로 여겨서 자동으로 생기기 떄문에 굳이 설정할 필요 없음
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=13)
    # open_time = models.TimeField(default=datetime.time)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 관련 쿼리셋에서 order_by를 지정하지 않을 때 
        # 적용될 디폴트 정렬
        ordering = ['-id']
