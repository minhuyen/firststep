from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

# Register your models here.
from firststep.models import Category, JournalArticle


class JournalArticleAdminForm(forms.ModelForm):
    summary = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = JournalArticle
        widgets = {
            'content': RedactorEditor(
                redactor_options={'lang': 'en',
                                  'focus': 'true',
                                  "imageUpload": "false",
                                  "linkFileUpload": "false",
                                  "fileUpload": "false", },
                upload_to='tmp/',
                allow_file_upload=False,
                allow_image_upload=False
            ),
        }


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['parent', 'name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ['name', '_parents_repr', 'pub_date']


class JournalArticleAdmin(admin.ModelAdmin):
    form = JournalArticleAdminForm
    fields = ['category', 'title', 'summary', 'content', 'small_img', 'article_img', 'show_img', 'pub_date']
    list_display = ['category', 'title', 'summary', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['title']
    ordering = ['-pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(JournalArticle, JournalArticleAdmin)
