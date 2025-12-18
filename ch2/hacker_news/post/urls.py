from django.urls import path
from post import views

urlpatterns = [
    path("", views.posts_view, name = "posts"), #전체 게시물 목록
    path("<int:post_id>/", views.post_view, name="post"), #상세 게시글 조회
]
