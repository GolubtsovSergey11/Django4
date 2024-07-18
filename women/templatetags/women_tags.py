from django import template
import women.views as views



#Создаем экземпляр класса Library (нужен для регистрации наших тэгов)
register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db

