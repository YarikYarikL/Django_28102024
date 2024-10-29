from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('items',views.list_of_items),
    path('item/<int:num>',views.single_item)
]
