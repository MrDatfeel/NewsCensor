from django.shortcuts import render
from .models import Article
from django.shortcuts import render, get_object_or_404

def news_list(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'news_list.html', {'articles': articles})

def news_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news_detail.html', {'article': article})