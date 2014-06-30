from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question


class JournalArticle(models.Model):
    category = models.ForeignKey(Category)
    summary = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    small_img = models.FileField()
    article_img = models.FileField()
    show_img = models.FileField()

    def __unicode__(self):
        return self.title




