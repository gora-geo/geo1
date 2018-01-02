from django.shortcuts import render


from news.models import *


def home(request): #ф-ция home принимает request-запррос из браузера  на странице home/ смотри фаил urls
    news_images=NewsImage.objects.filter(is_active=True,is_main=True)  #переменая куда входят все объеты класса ProductImage c галками активный и главная

    return render(request, 'home/home.html', locals())  #ответ на request отрисовка страница передача перемееной