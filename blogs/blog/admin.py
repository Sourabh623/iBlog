from django.contrib import admin
from .models import Category, Post

# configuration of category and post for admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'created_at')
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 30


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'content', 'url', 'created_at')
    search_fields = ('title',)
    list_filter = ('cat_id',)
    list_per_page = 30

    class Media:
        # Tiny Api Key
        API_KEY = "0ous51oh5nwilqfy3fm0o7f59hkx02rq6b1kct0ln0x4p20x"
        js = ('https://cdn.tiny.cloud/1/{}/tinymce/5/tinymce.min.js'.format(API_KEY), 'js/script.js')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
