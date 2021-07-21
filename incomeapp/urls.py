from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item',views.add_item, name='add item'),
    path('delete_item/<int:income_item_id>/',views.delete_item, name='delete item'),
]