from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from firststep.models import Category,JournalArticle
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger('firststep.views')
def home(request):
    try:
        category1 = Category.objects.get(name="dat-nen-du-an")
    except Category.DoesNotExist:
        categoryName1 = ""
        list1 = []
    else:
        categoryName1 = category1.name
        list1 = category1.journalarticle_set.order_by('-pub_date')[:4]

    try:
        category2 = Category.objects.get(name="biet-thu-ven-bien")
    except Category.DoesNotExist:
        categoryName2 = ""
        list2 = []
    else:
        categoryName2 = category2.name
        list2 = category2.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category3 = Category.objects.get(name="nha-dat-can-ban")
    except Category.DoesNotExist:
        categoryName3 = ""
        list3 = []
    else:
        categoryName3 = category3.name
        list3 = category3.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category4 = Category.objects.get(name="can-ho")
    except Category.DoesNotExist:
        categoryName4 = ""
        list4 = []
    else:
        categoryName4 = category4.name
        list4 = category4.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category5 = Category.objects.get(name="tin-tuc")
    except Category.DoesNotExist:
        categoryName5 = ""
        list5 = []
    else:
        categoryName5 = category5.name
        list5 = category5.journalarticle_set.order_by('-pub_date')[:4]

    try:
        category6 = Category.objects.get(name="home")
    except Category.DoesNotExist:
        categoryName6 = ""
        list6 = []
    else:
        categoryName6 = category6.name
        list6 = category6.journalarticle_set.order_by('-pub_date')[:4]

    context = {'list1': list1, 'categoryName1': categoryName1, 'list2': list2, 'categoryName2': categoryName2,
               'list3': list3, 'categoryName3': categoryName3, 'list4': list4, 'categoryName4': categoryName4,
               'list5': list5, 'categoryName5': categoryName5, 'list6': list6, 'categoryName6': categoryName6}
    return render(request, 'firststep/home.html', context)


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
        category = Category.objects.get(name=" dat-nen-du-an")
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
    
