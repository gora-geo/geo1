from django.contrib import admin  #импорт интерфейса администрирования
from .models import *             #импорт файла models из(*-текушей паки в данном случаее landing)

class NewsImageInline(admin.TabularInline): #TabularInlineподкласс InlineModelAdmin(Интерфейс администратора позволяет редактировать связанные объекты на одной странице с родительским объектом. Это называется “inlines”.)
    model = NewsImage
    extra = 0       # Указывает количество пустых форм для добавления объектов в наборе форм.

class NewsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
    inlines = [NewsImageInline]    #добовление в данную таблицу в админке (таблицу продукта) таблицы (фотографии продукта)
                                    #тоесть в таблице продукта появиться таблица фотографии и она добавит фотографии при нажати на id или при добовлениии товара
                                #олько для этого надо описать  класс ProductImageInline(как этосделановыше)
    class Meta:
        model = News

admin.site.register(News, NewsAdmin)


class NewsImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NewsImage._meta.fields]

    class Meta:
        model = NewsImage

admin.site.register(NewsImage, NewsImageAdmin)