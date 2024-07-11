from django.urls import path
from . import views

urlpatterns = [
    path("", views.Women.index),
    path("cat/<int:cats_id>/", views.Women.categories),
    path("num/<slug:nums_id>/", views.Women.random_int),
    path("cars/", views.Women.cars),
]
