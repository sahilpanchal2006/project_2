from django.shortcuts import render, get_object_or_404

from .models import BlogPost
from services.models import ServiceCategory, Product


def home(request):
    """Home page view with latest 3 published blog posts, service categories, and featured products."""
    latest_posts = BlogPost.objects.filter(status='published')[:3]
    service_categories = ServiceCategory.objects.all()
    featured_products = Product.objects.filter(is_featured=True)[:3]
    context = {
        'latest_posts': latest_posts,
        'services': service_categories,
        'featured_products': featured_products,
    }
    return render(request, 'home.html', context)


def blog_list(request):
    """List all published blog posts."""
    posts = BlogPost.objects.filter(status='published')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display a single blog post by its slug."""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)
