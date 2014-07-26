# -*- coding: utf-8 -*-
from datetime import datetime
from django.core import validators
from django.db import models
from redactor.fields import RedactorField
from geoposition.fields import GeopositionField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    cat_key = models.CharField(max_length=200, verbose_name='Key')
    position = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=datetime.now)
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


class Location(models.Model):
    name = models.CharField(max_length=150)
    position = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class JournalArticle(models.Model):
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location, blank=True, null=True)
    summary = models.CharField(max_length=350)
    content = models.CharField(max_length=10000, verbose_name="Content")
    pub_date = models.DateTimeField('date published', default=datetime.now)
    title = models.CharField(max_length=50)
    small_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    article_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    show_img = models.FileField(upload_to='journal_article/%Y/%m/%d')
    area = models.IntegerField(default=0, verbose_name=u'Diện tích (m2)')
    price = models.FloatField(default=0.0, verbose_name=u'Giá(Triệu)')
    #short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
        return self.title


class ContactInfo(models.Model):
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    description = models.CharField(max_length=10000, verbose_name="Content")
    position = GeopositionField()

    def __unicode__(self):
        return self.name   

class Home(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=150)
    position = models.IntegerField(default=0)
    show_img = models.FileField(upload_to='home/%Y/%m/%d')
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def __unicode__(self):
        return self.title

