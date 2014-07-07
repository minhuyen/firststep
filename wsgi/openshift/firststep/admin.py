from django.contrib import admin

# Register your models here.
from firststep.models import Category, JournalArticle

admin.site.register(Category)
admin.site.register(JournalArticle)
