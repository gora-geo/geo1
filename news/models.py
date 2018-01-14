from django.db import models  #импорт приложения models



class News(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None,verbose_name='Название')
    description = models.TextField(blank=True, null=True, default=None,verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='обновлен')

    def __str__(self):
        return "%s" % ( self.name)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsImage(models.Model):
    news = models.ForeignKey(News, blank=True,on_delete=models.DO_NOTHING, null=True, default=None,verbose_name='Название')
    image = models.ImageField(upload_to='products_images/',verbose_name='Картинка')  #путь к картинке в папек static/products_images/
    is_main=models.BooleanField(default=False,verbose_name='Главная')   #поле модели(таблицы)-главная тоест какая картинка если их несколько будет выводиться первой
    is_active = models.BooleanField(default=True,verbose_name='активный')  #активна ли картинка
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='обновлен')

    def __str__(self):
        return "%s" % self.id #настраивает отображение в таблице (home/productss/product(потомA lot of orderss)id( продукта)

    class Meta:                        #доп настройки для модели
        verbose_name = 'Фотография'         #Читабельное название модели, в единственном числе:
        verbose_name_plural = 'Фотографии'   #Название модели в множественном числ (админка будет выгладить products/фотографии/если добавить и вверху-фотография

