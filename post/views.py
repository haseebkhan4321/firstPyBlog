from django.shortcuts import render

from post.models import Post


# Create your views here.
def show(request, slug):
    post = Post.objects.filter(slug=slug, published_at__isnull=False).first()
    return render(request, 'post-detail.html', {'post': post})


def search(request):
    pass
