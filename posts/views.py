# -*-coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from posts.models import Article


# Create your views here.
# 创建一个获取文章详情的方法
def article_detail(request, article_id):
    #    try:
    #        article = Article.objects.get(id=article_id)
    #        context = {"article": article}
    #        return render(request, "article_detail.html", context)
    #    except Article.DoesNotExist:
    #        raise Http404("文章不存在")
    article = get_object_or_404(Article, id=article_id)
    context = {"article": article}
    return render(request, "article_detail.html", context)
