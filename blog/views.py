from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog_home.html", {"title":"Blog","posts":posts})

def render_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog_posts.html", {"title":post.title,"post": post})
    