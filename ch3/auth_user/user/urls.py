from django.urls import path, include
from user import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"), # 내가 만든 기능 → 직접 view 연결
    path("users/", include("django.contrib.auth.urls")), # 프레임워크가 제공하는 기능 묶음
    path("users/sign_up/", views.SignUpView.as_view(), name="sign_up"),
]
