from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-888-888-88-88",
    "email": "ivanovip@mail.ru"
}

def home(request):
    return render(request,"index.html")

def list_of_items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request,"items_list.html", context)

def single_item(request, num):
    try:
        single_item = Item.objects.get(id=num)
        item_colors = []
        if single_item.colors.exists():
            item_colors = single_item.colors.all()
    except ObjectDoesNotExist:
        return render(request,"item_not_exists.html", {"num":num})
    else:
        context = {"single_item": single_item,
                   "item_colors": item_colors,
                   }
        return render(request,'item_info.html',context)
        

def author_info (request):
    context = {
        "author" : author
    }
    return render(request,"author_info.html", context)