# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    #设置url
    url(r'^article/(?P<article_id>\d+)$',\
        views.ArticleDetailView.as_view(), name = 'detail'),
    ]
