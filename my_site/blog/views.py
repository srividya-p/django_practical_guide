from django.shortcuts import render

from blog.models import Author, Post, Tag

# Create your views here.

def start_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post-details.html", {
        "post": post,
        "tags": post.tags.all()
    })
