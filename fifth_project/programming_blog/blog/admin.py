from django.contrib import admin
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_created', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex', 'content__iregex')  # iregex - регистронезависимый поиск
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name__iregex',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
