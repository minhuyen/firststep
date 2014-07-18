from firststep.models import Category

__author__ = 'shin'


def categoryList(request):
    return {'categoryList': Category.objects.all().order_by('position')}
