# -*- coding:utf-8 -*-
from django.db import models


class Article(models.Model):
    #设置status
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text="可选，如若为空将摘取正文的前54个字符")
    #views和like不显示
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    
    #保存body到摘要里面
    def save(self, *args, **kwargs):
        self.abstract = self.abstract or self.body[:54]
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title.encode("utf-8")

    class Meta:
        #默认排序方式
        ordering = ['-last_modified_time']

