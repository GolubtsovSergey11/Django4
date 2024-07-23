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


