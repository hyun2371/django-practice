from django.db import models

# Create your models here.
# 게시물
# - 제목, 본문, 작성자 이름, 좋아요 개수, 게시물 생성시간

class Post(models.Model): #models.Model 상속 받아 class 정의
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    author_name = models.CharField(max_length=32)
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #원하는 형태로 데이터 출력 형태 바꿈
        return f"{self.id}, {self.title}"
