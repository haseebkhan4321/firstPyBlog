from django.db.models import Count
from django.shortcuts import render

from category.models import Category
from tag.models import Tag
from post.models import Post


def homepage(request):
    categories = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0, post__published_at__isnull=False)
    tags = Tag.objects.filter(post__isnull=False, post__published_at__isnull=False)
    trendingPosts = Post.objects.all().order_by('-total_views')[:3]
    editorPickPost = Post.objects.filter(flag_1=True).order_by('-total_views').first()
    popularPost = Post.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews').first()
    # allPosts = Post.objects.all().order_by('-publised_at')
    return render(request, 'homepage.html',{
        'categories': categories,
        'tags': tags,
        'trendingPosts': trendingPosts,
        'editorPickPost': editorPickPost,
        'popularPost': popularPost
    })
