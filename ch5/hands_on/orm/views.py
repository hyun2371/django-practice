from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60) # 캐시 페이지 - 60초 안에 동일 작업 캐싱
def home_view(request):
    print("오래 걸리는 작업 진행 중...")
    return render(request, "email.html")