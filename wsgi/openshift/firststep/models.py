from django.core import validators
from django.db import models
from redactor.fields import RedactorField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    cat_key = models.CharField(max_length=200, verbose_name='Key', blank=True)
    pub_date = models.DateTimeField('date published')
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children")

    class Admin:
        list_display = ('name', '_parents_repr')

    def get_absolute_url(self):
        if self.parent_id:
            return "/%s/%s/" % (self.parent.cat_key, self.cat_key)
        else:
            if self.cat_key == "":
                return ""
            else:
                return "/%s/" % (self.cat_key, )

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p.name)
            more = self._recurse_for_parents(p)
            p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def get_separator(self):
        return ' :: '

    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = "Category parents"

    def save(self):
        p_list = self._recurse_for_parents(self)
        if self.name in p_list:
            raise validators.ValidationError("You must not save a category in itself!")
        super(Category, self).save()

    def __unicode__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.name)
        return self.get_separator().join(p_list)


class JournalArticle(models.Model):
    category = models.ForeignKey(Category)
    summary = models.CharField(max_length=150)
    content = models.CharField(max_length=10000, verbose_name="Content")
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    small_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    article_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    show_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    #short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
        return self.title




