from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item',views.add_item, name='add item'),
]