from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from firststep.models import Category,JournalArticle


def home(request):
    return render(request, 'firststep/home.html')


def houseForSaleList(request):
    category = Category.objects.get(name="home")
    hfs_list = category.journalarticle_set.order_by('-pub_date')[:3]
    #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
    context = RequestContext(request, {'hfs_list': hfs_list})
    return render(request, 'firststep/nhadat-canban.html', context)


# def detail(request, ja_id):
#     ja = get_object_or_404(JournalArticle, pk=ja_id)
#     return render(request, 'firststep/detail.html', {'ja':ja})