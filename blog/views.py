from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post


def post_list(request):
    posts = Post.published.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.is_publish() and not request.user.is_staff:
        raise Http404("Page not found")
    return render(request, 'blog/post_details.html', {'post': post})
