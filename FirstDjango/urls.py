from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('items',views.list_of_items, name='list_of_items'),
    path('item/<int:num>',views.single_item, name ='single_item'),
    path('author_info',views.author_info, name = 'author_info')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
