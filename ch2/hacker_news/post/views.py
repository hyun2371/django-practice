from gc import get_objects

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from post.models import Post
# Create your views here.

def posts_view(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(
        request, "post_list.html", context
    )

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post" : post} #html key 변수와 동일해야 함
    return render(
        request, "post_detail.html", context
    )
