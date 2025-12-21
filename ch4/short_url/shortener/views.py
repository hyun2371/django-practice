from django.views import View
from django.shortcuts import render

from shortener.models import ShortURL


class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all() # shortUrlRepository.findAll();
        return render(
            request, "home.html",
            {"short_urls":short_urls}
        )

