from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('items',views.list_of_items),
    path('item/<int:num>',views.single_item),
    path('author_info',views.author_info)
]
