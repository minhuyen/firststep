from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from firststep.models import Category,JournalArticle
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger('firststep.views')
def home(request):
    return render(request, 'firststep/home.html')


def houseForSaleList(request):
    try:
        category = Category.objects.get(name="nha-dat-can-ban")
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}

    return render(request, 'firststep/news.html', context)


def houseForRentList(request):
    try:
        category = Category.objects.get(name="nha-dat-cho-thue")
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)

def coastalVillaList(request):
    try:
        category = Category.objects.get(name="biet-thu-ven-bien")
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)

def apartmentList(request):
    try:
        category = Category.objects.get(name="can-ho")
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)


def projectLandList(request):
    try:
        category = Category.objects.get(name="dat-nen-du-an")
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)


def news(request):
    try:
        category = Category.objects.get(name="news")
    except Category.DoesNotExist:
        context = {'list': [], 'title': "Tin tuc", "error_message": ""}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        #hfs_list = JournalArticle.objects.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)


def detail(request, ja_id):
    ja = get_object_or_404(JournalArticle, pk=ja_id)
    return render(request, 'firststep/detail.html', {'ja': ja})
#Hanh.Nguyen add Contact Page


def contact(request):
    return render(request, 'firststep/contact.html')

def sendMail(request):
    emailAddress = request.POST.get("emailAddress", "")
    comment = request.POST.get("comment", "")
    name = request.POST.get("name", "")
    #send email
    send_mail(name, comment, emailAddress,
    [settings.EMAIL_HOST_USER], fail_silently=False)

    logger.debug("Come here!!!")
    return render(request, 'firststep/contact.html')
    
