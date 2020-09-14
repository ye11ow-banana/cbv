from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Блог, который может создать каждый пользователь'''
    list_display = ('topic', 'user', 'pub_date')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Категория блога'''
    list_display = ('title',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    '''Тег блога'''
    list_display = ('title',)


admin.site.site_title = 'Blog'
admin.site.site_header = 'Blog'