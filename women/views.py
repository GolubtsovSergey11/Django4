from django.http import HttpResponse
from django.shortcuts import render

class Women():
    def index(request):
        return HttpResponse("Стариница приложения women")

    def categories(request):
        return HttpResponse("<h1>Категории товаров</h1>")
