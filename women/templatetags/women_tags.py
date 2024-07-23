from django import template
import women.views as views



#Создаем экземпляр класса Library (нужен для регистрации наших тэгов)
register = template.Library()

#Простой тэг
@register.simple_tag(name="getcat")
def get_categories():
    return views.cats_db

#Простой тэг
@register.simple_tag(name='sportsmen')
def sportsmen():
    return views.world_sport


#включающий тэг

#в декоратор передаем путь шаблона в который вернется словарь {'categories': cats}
#то есть этот тэг будет возвращать сформированную html страницу list_categories.html
@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = views.cats_db
    return {'categories': cats}
