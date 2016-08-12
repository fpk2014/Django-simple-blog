# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article
import markdown2



class IndexView(ListView):
    #联系html
    template_name = "blog/index.html"

    def get_queryset(self):
        article_list = Article.objects.filter(status = 'p')
        for article in article_list:
            article.body = markdown2.markdown(article.body)
            article.abstract = markdown2.markdown(article.abstract)
        return article_list


class ArticleDetailView(DetailView):
    #继承Article类
    model = Article
    template_name = "blog/detail.html"
    #设置pk的数据
    pk_url_kwarg = 'article_id'

    def get_object(self):
        # 实例化get_object()
        article = super(ArticleDetailView, self).get_object()
	article.views += 1
	article.save()
        article.body = markdown2.markdown(article.body)
        return article
