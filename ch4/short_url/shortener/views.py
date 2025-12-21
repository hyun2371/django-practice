from django.views import View
from django.shortcuts import render, redirect
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
