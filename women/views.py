import random
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


class Women():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def index(request):
        # t = render_to_string('women/index.html')
        # return HttpResponse(t)
        return render(request, 'women/index.html')

    def about(request):
        data = {'title': "о сайте)", "about": "интересно узнать о нас?",
                "float": 28.54,
                "menu": ["Главная", " Контакты"],
                "lst": [23, "abc", True],
                "str": "I'm Sergey",
                "dict": {"key-1" : "value_1", "key-2" : "value_2"},
                "obj": Women(1, 2),
                "url": slugify("The best")}
        return render(request, "women/about.html", data)

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

    def cars(request, cars_id):
        return HttpResponse(f"У Вас Porshe 911?") if cars_id == 911 else redirect('home')

    def sport(request):
        uri = reverse('num', args=('5h45', ))
        return HttpResponseRedirect(uri)

    def page_not_found(request, exception):
        return HttpResponseNotFound("Ваша страница не найдена")



