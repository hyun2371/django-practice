from django.db.models import F
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from shortener.forms import ShortURLForm
from shortener.models import ShortURL


class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all() # shortUrlRepository.findAll();
        context = {
            "short_urls": short_urls, # entity
            "form" : ShortURLForm, # DTO, 검증
        }

        return render(
            request, "home.html",
            context
        )

class ShortURLCreateView(View):
    def post(self, request):
        form = ShortURLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False) # 객체 생성o, 커밋 x -> 값 채우고 저장할 목적
            while True: #중복 제거
                code = ShortURL.generate_code()
                if not ShortURL.objects.filter(code=code).exists():
                    break

            obj.code = code
            obj.save()
            return redirect("home")

class ShortURLDetailView(View):
    # 127.0.0.1:8000/abcd/ -> google.com
    def get(self, request, code): # url로 code 파라미터 받아옴
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.access_count = F("access_count") + 1 #원자적 갱신
        short_url.save()
        return redirect(short_url.original_url)

class ShortURLDeleteView(View):
    def post(self, request, code): # form은 GET, POST 메서드만 사용 가능
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return redirect("home")