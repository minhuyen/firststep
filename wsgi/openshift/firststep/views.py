from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from firststep.models import Category,JournalArticle, Home, ContactInfo
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import logging

logger = logging.getLogger('firststep.views')


def home(request):
    try:
        category1 = Category.objects.get(cat_key="dat-nen-du-an")
    except Category.DoesNotExist:
        categoryName1 = ""
        list1 = []
    else:
        categoryName1 = category1.name
        list1 = category1.journalarticle_set.order_by('-pub_date')[:4]

    try:
        category2 = Category.objects.get(cat_key="biet-thu-ven-bien")
    except Category.DoesNotExist:
        categoryName2 = ""
        list2 = []
    else:
        categoryName2 = category2.name
        list2 = category2.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category3 = Category.objects.get(cat_key="nha-dat-can-ban")
    except Category.DoesNotExist:
        categoryName3 = ""
        list3 = []
    else:
        categoryName3 = category3.name
        list3 = category3.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category4 = Category.objects.get(cat_key="can-ho")
    except Category.DoesNotExist:
        categoryName4 = ""
        list4 = []
    else:
        categoryName4 = category4.name
        list4 = category4.journalarticle_set.order_by('-pub_date')[:1]

    try:
        category5 = Category.objects.get(cat_key="tin-tuc")
    except Category.DoesNotExist:
        categoryName5 = ""
        list5 = []
    else:
        categoryName5 = category5.name
        list5 = category5.journalarticle_set.order_by('-pub_date')[:4]

    try:
        home = Home.objects.all()
    except Home.DoesNotExist:
        list6 = []
    else:
        list6 = home.order_by('-position')[:4]

    context = {'list1': list1, 'categoryName1': categoryName1, 'list2': list2, 'categoryName2': categoryName2,
               'list3': list3, 'categoryName3': categoryName3, 'list4': list4, 'categoryName4': categoryName4,
               'list5': list5, 'categoryName5': categoryName5, 'list6': list6}
    return render(request, 'firststep/home.html', context)


def viewCategory(request, cat_key):
    try:
        category = Category.objects.get(cat_key=cat_key)
    except Category.DoesNotExist:
        context = {'list': []}
    else:
        list = category.journalarticle_set.order_by('-pub_date')[:3]
        context = {'list': list}
    return render(request, 'firststep/news.html', context)


def news(request):
    try:
        category = Category.objects.get(cat_key="tin-tuc")
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
    try:
        contactGeo = ContactInfo.objects.all()[0]
        return render(request, 'firststep/contact.html',{'contact':contactGeo})
    except:
        return render(request, 'firststep/contact.html',{'contact':0})
    try:
        contactGeo = ContactInfo.objects.all()[0]
        if request.method == 'POST':
            try:
                emailAddress = request.POST.get("emailAddress", "")
                comment = request.POST.get("comment", "")
                name = request.POST.get("name", "")
                phone = request.POST.get("mobile", "")
                subject, from_email, to = 'Message from'+" "+name, settings.EMAIL_HOST_USER, 'minhuyendo@gmail.com'
                text_content = 'You have received request from customer.'
                html_content = '<p>Hi!</p><p>Below is the customer contact information</p><p><strong>Name:</strong> '+name+'</p><p><strong>Email:</strong> '+emailAddress+'</p><p><strong>Phone:</strong> '+phone+'</p><p><strong>Message:</strong></p> <div>'+comment+'</div><p>-----</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                return render(request, 'firststep/contact.html',{'result':1,'contact':contactGeo})
            except:
                return render(request, 'firststep/contact.html',{'result':0,'contact':contactGeo})
        else:
             return render(request, 'firststep/contact.html',{'contact':contactGeo})
    except:
        return render(request, 'firststep/contact.html',{'contact':0})