from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'blog_post.html', {
        'post': post_obj
    })