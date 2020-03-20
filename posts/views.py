# -*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from posts.models import Article


# Create your views here.
# 创建一个获取文章详情的方法
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("文章不存在")
    else:
        return HttpResponse("文章标题:%s <br> 文章内容:%s" % (article.title, article.content))
