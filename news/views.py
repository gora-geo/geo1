from django.shortcuts import render
from news.models import *

def news(request,news_id):  #ф-ция promoopen принимает request-запррос+product_id из браузера на странице product/1/(напирмер) смотри фаил urls
    news=News.objects.get(id=news_id)   #передаеться переменная что представляет из себя объект класса продукта(с тем id который передан от браузера)
    session_key=request.session.session_key    #получение ключа сети
    if not session_key:                        #если нет ключасети...
        request.session.cycle_key()            #...то нам надо создать ключ сети вручную(эта  строчка создает его)
    print(request.session.session_key)         #вывод ключа сети в терминал
    return render(request,'news/news.html',locals())