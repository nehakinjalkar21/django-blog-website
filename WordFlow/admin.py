from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter= ('cat',)

    class Media:
        js=('https://cdn.tiny.cloud/1/mnnod8csxw2fn1wo3xs0ztx554ebzocs9gr1wv9le1r2f1cr/tinymce/7/tinymce.min.js','js/script.js',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
