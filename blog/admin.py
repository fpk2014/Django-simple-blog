from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modified_time','status')
    list_filter = ['last_modified_time']
    fields = ['title','body','status','abstract','topped']

admin.site.register(Article, ArticleAdmin)    
