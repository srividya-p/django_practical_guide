from django.urls import path

from . import views

urlpatterns = [
    path("", views.start_page, name="start-page"),
    path("posts", views.posts, name="all-posts"),
    path("posts/<slug:slug>", views.post_details, name="post-details"),
]
