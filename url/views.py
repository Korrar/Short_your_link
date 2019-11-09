from django.shortcuts import redirect
from django.shortcuts import render
from url.forms import UrlForm
from url.models import Links ,Shortcut
from django.core import exceptions
import random
import string

my_domian = 'https://short-your-url-5.herokuapp.com/'


def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def short_link():
    st = randomString()
    check = True
    while check == True:
        try:
            short = Shortcut.objects.get(shortcut=st)
            st = randomString()
            check = True
        except exceptions.ObjectDoesNotExist:
            check = False
            obj = Shortcut()
            obj.shortcut = st
            obj.save()
            return st


def home_view(request):
    print(request.user)
    form = UrlForm(request.POST or None)
    if form.is_valid():
        form.save()
        try:
            obj = Links.objects.latest('link_id')
            obj.url_shorted_link = '{}{}'.format(my_domian,short_link())
            obj.save()
            context = {'form': form,
                       'shorted': obj.url_shorted_link, }
            return render(request, 'home.html', context)
        except exceptions.ObjectDoesNotExist:
            pass
    context = {'form': form, }

    return render(request, 'home.html', context)


def redirecting_view(request, string ):
    try:
        obj = Links.objects.get(url_shorted_link ='{}{}'.format(my_domian,string))
        return redirect('{}'.format(obj.url_link))
    except exceptions.ObjectDoesNotExist:
        redirect('')




