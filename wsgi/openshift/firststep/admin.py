from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

# Register your models here.
from firststep.models import Category, JournalArticle, Location, Home,ContactInfo

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
        (None,               {'fields': ['parent', 'name', 'cat_key', 'position']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ['name', '_parents_repr', 'position', 'pub_date']

class LocationAdmin(admin.ModelAdmin):
    fields = ['name', 'position']
    list_display = ['name', 'position']


class JournalArticleAdmin(admin.ModelAdmin):
    form = JournalArticleAdminForm
    fields = ['category', 'title', 'summary', 'content', 'small_img', 'article_img', 'show_img', 'area',
              'price', 'pub_date', 'location']
    list_display = ['category', 'title', 'summary', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['title']
    ordering = ['-pub_date']
class ContactInfoAdminFrom(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

class ContactInfoAdmin(admin.ModelAdmin):
    form = ContactInfoAdminFrom
    fields = ['company', 'address', 'name', 'phone', 'email', 'website', 'description', 'position']

class HomeAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'position', 'show_img', 'pub_date']
    list_display = ['category', 'title', 'position', 'pub_date']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(JournalArticle, JournalArticleAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
