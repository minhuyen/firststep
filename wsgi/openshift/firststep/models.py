from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name


class JournalArticle(models.Model):
    category = models.ForeignKey(Category)
    summary = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    small_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    article_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    show_img = models.FileField(upload_to='journal_article/%Y/%m/%d')

    def __unicode__(self):
        return self.title




