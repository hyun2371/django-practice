from django.urls import path
from shortener import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # 경로, 처리할 뷰, 별칭
    path("short-urls/", views.ShortURLCreateView.as_view(), name="shorten_url"),
]
