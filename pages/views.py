from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(req):
    return HttpResponse('anasayfadasın')
def iletisim(req):
    return HttpResponse('iletisim sayfası')
def hakkimizda(req):
    return HttpResponse('hakkimizda sayfasındasın')