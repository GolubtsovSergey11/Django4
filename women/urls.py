from django.urls import path
from . import views

urlpatterns = [
    path("", views.Women.index),
    path("cat/", views.Women.categories),
]
