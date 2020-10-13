from django.contrib import admin
from .models import Article

# display all fields from Article model
class ArticleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Article._meta.get_fields()]

admin.site.register(Article, ArticleAdmin)
