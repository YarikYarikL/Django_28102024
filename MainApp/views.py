from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-888-888-88-88",
    "email": "ivanovip@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity":5},
   {"id": 2, "name": "Куртка кожаная", "quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
   {"id": 7, "name": "Картофель фри", "quantity":0},
   {"id": 8, "name": "Кепка", "quantity":124},
]

def home(request):
    return render(request,"index.html")

def list_of_items(request):
    context = {
        "items": items
    }
    return render(request,"items_list.html", context)

def single_item(request, num):
    context = {
        "items" : items,
        "num" : num
    }
    for i in items:
        if i["id"] == num:
            return render(request,"item_info.html", context)
    return render(request,"item_not_exists.html", context)

def author_info (request):
    context = {
        "author" : author
    }
    return render(request,"author_info.html", context)