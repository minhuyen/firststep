from django.db import models
from redactor.fields import RedactorField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name


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




