from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<b>Тест</b>")

def about(request):
    return HttpResponse("<b>Тест страницы About</b>")

def contacts(request):
    return HttpResponse("<b>Тест страницы Contacts</b>")

