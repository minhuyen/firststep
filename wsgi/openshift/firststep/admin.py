from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

# Register your models here.
from firststep.models import Category, JournalArticle

class JournalArticleAdminForm(forms.ModelForm):
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


class JournalArticleAdmin(admin.ModelAdmin):
    form = JournalArticleAdminForm

admin.site.register(Category)
admin.site.register(JournalArticle, JournalArticleAdmin)
