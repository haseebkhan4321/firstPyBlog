from django.db.models import Count
from django.shortcuts import render

from category.models import Category
from tag.models import Tag
from post.models import Post


def homepage(request):
    categories = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0, post__published_at__isnull=False)
    tags = Tag.objects.filter(post__isnull=False, post__published_at__isnull=False)
    editorPickPost = Post.objects.filter(flag_1=True,published_at__isnull=False).order_by('-total_views').first()
    trendingPosts = Post.objects.filter(published_at__isnull=False).order_by('-total_views')[:3]
    popularPost = Post.objects.annotate(num_reviews=Count('review')).filter(published_at__isnull=False).order_by('-num_reviews').first()
    topRatedPosts = Post.objects.all()
    allPosts = Post.objects.all()
    return render(request, 'homepage.html',{
        'categories': categories,
        'tags': tags,
        'trendingPosts': trendingPosts,
        'editorPickPost': editorPickPost,
        'popularPost': popularPost,
        'topRatedPosts': topRatedPosts,
        'allPosts':allPosts
    })
