from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(req):
    return HttpResponse('anasayfa ekranı')

def kurslar(req):
    return HttpResponse('Kurs Listesi')