from django.contrib import admin

from blog.models import Tag, Post, Author

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags")

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
