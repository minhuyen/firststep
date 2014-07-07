from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from firststep.models import Category,JournalArticle


def home(request):
    return render(request, 'firststep/home.html')


def houseForSaleList(request):
    try:
        category = Category.objects.get(name="nha-dat-can-ban")
    except Category.DoesNotExist:
        context = {'hfs_list': []}
    else:
        hfs_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'hfs_list': hfs_list}

    return render(request, 'firststep/nhadat-canban.html', context)


def houseForRentList(request):
    try:
        category = Category.objects.get(name="nha-dat-cho-thue")
    except Category.DoesNotExist:
        context = {'hfr_list': []}
    else:
        hfr_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'hfr_list': hfr_list}
    return render(request, 'firststep/nhadat-canban.html', context)


def coastalVillaList(request):
    try:
        category = Category.objects.get(name="biet-thu-ven-bien")
    except Category.DoesNotExist:
        context = {'cv_list': []}
    else:
        cv_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'cv_list': cv_list}
    return render(request, 'firststep/nhadat-canban.html', context)


def apartmentList(request):
    try:
        category = Category.objects.get(name="can-ho")
    except Category.DoesNotExist:
        context = {'apartment_list': []}
    else:
        apartment_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'apartment_list': apartment_list}
    return render(request, 'firststep/nhadat-canban.html', context)


def projectLandList(request):
    try:
        category = Category.objects.get(name=" dat-nen-du-an")
    except Category.DoesNotExist:
        context = {'pl_list': []}
    else:
        pl_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'pl_list': pl_list}
    return render(request, 'firststep/nhadat-canban.html', context)


def news(request):
    try:
        category = Category.objects.get(name="news")
    except Category.DoesNotExist:
        context = {'hfs_list': [], 'title': "Tin tuc", "error_message": ""}
    else:
        hfs_list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'hfs_list': hfs_list}

    return render(request, 'firststep/nhadat-canban.html', context)


def detail(request, ja_id):
    ja = get_object_or_404(JournalArticle, pk=ja_id)
    return render(request, 'firststep/detail.html', {'ja': ja})
#Hanh.Nguyen add Contact Page
def contact(request):
    return render(request, 'firststep/contact.html')
