from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from django.db.models import Q

def article_list(request):
    articles = Article.objects.filter(status='published').order_by('-created_at')
    categories = Category.objects.all()
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        articles = articles.filter(category__slug=category_slug)
    
    # Pagination
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    context = {
        'articles': articles,
        'categories': categories,
        'query': query,
        'category_slug': category_slug,
    }
    return render(request, 'blog/article_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='published')
    comments = article.comments.filter(is_approved=True)
    
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                article=article,
                author=request.user,
                content=content
            )
            messages.success(request, 'Your comment has been submitted for review.')
            return redirect('article_detail', slug=slug)
    
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'blog/article_detail.html', context)

@login_required
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        featured_image = request.FILES.get('featured_image')
        
        if title and content and category_id:
            category = get_object_or_404(Category, id=category_id)
            article = Article.objects.create(
                title=title,
                content=content,
                category=category,
                author=request.user,
                slug=title.lower().replace(' ', '-'),
                featured_image=featured_image
            )
            messages.success(request, 'Article created successfully!')
            return redirect('article_detail', slug=article.slug)
    
    categories = Category.objects.all()
    return render(request, 'blog/article_form.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, status='published')
    
    # Pagination
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'blog/category_detail.html', context)
