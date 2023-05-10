from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def archive(request, year):
    if int(year) >= 2024:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def index(request):
    return render(request, 'pages/index.html', {'title': 'Заголовок'})


def categories(request, categ):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Страница приложения pages</h1><p>{categ}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
