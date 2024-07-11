import random
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

class Women():

    def index(request):
        return HttpResponse("Стариница приложения women")

    def categories(request, cats_id):
        return HttpResponse(f"<h1>Категории товаров c id {cats_id}</h1>")

    def random_int(request, nums_id):
        start = 0
        stop = 100
        rand = random.randint(start, stop)
        if rand > 90:
            raise Http404()
        return HttpResponse(f"<h2> Выбрали случайное число от {start} до {stop}, "
                            f"и получили число {rand}<br>"
                            f"slug {nums_id}")

    def cars(request):
        return HttpResponse(f"Продолжаем обучение")

    def page_not_found(request, exception):
        return HttpResponseNotFound("Ваша страница не найдена")



