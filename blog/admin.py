from django.contrib import admin
from django.utils.safestring import mark_safe#<<<<

from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget# ca sa mearga importu la acest fignea tr sa scot marca de pe siteblog


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#asta ca sa faca slugu automat
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'foto'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#asta ca sa faca slugu automat


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#asta ca sa faca slugu automat


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
