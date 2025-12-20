from gc import get_objects

from django.db.models import F
from django.http import HttpResponse, request, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from post.forms import PostForm
# Create your views here.

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {"posts" : posts, "form": PostForm}
        return render(
            request, "post_list.html", context
        )
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): #유효성 검사 통과
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            author_name = form.cleaned_data["author_name"]

            post = Post.objects.create(
            title=title,body=body,author_name=author_name
            )
            context = {"post" : post, "form": PostForm} #context -> 뷰에서 만든 데이터를 html로 전달

            return render(
                request, "post_detail.html", context
            )

        return redirect("posts") # 엔드포인트

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post" : post} #html key 변수와 동일해야 함
    return render(
        request, "post_detail.html", context
    )

def post_like_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.points = F("points") + 1 # 원자적 연산
    post.save()
    post.refresh_from_db()
    return render(
        request, "post_detail.html", {"post": post}
    )
