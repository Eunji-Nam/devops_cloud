from django.db import models
from blog.upload_to import uuid_name_upload_to

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to) # 'blog/post/%Y/%m/%d/%H')
    # upload_to='문자열' -> 파일이 저장되는 폴더의 경로
    # upload_to='blog/post/%Y'   /%Y/%m/%d/%H 를 이용해 파일을 어떻게 나누어 저장할 것인지 지정
    created_at = models.DateTimeField(auto_now_add=True) # 생성할 때 자동 지정
    updated_at = models.DateTimeField(auto_now=True) # 수정할 때 자동 지정

