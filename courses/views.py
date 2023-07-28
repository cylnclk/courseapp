from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data = {
    'programlama' : 'Programlama Kategorisindeki Kurslar',
    'web-gelistirme' : 'Web-geliştirme Kategorisindeki Kurslar',
    'mobil' : 'Mobile Kategorisindeki Kurslar',
}
def kurslar(req):
    return HttpResponse('Kurs Listesi')
def details(req, kurs_adi):
    return HttpResponse(f'{kurs_adi} Kurs Detay Sayfası')
def mobil(req):
    return HttpResponse('mobil Uygulama Sayfası')
#category parametre olarak alıyoruz
def getCoursesByCategory(request , category_name):
    try:
        category_text = data[category_name]
        return HttpResponse( category_text)
    except:
        return HttpResponseNotFound("Yanlış Kategori")
def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori (id)si  Seçimi")
    category_name = category_list[category_id-1]
    redirect_url = reverse('courses_by_name', args=[category_name])
    return  redirect(redirect_url)
    #return redirect('/kurslar/kategori/'+ category_name)
    #url name vererek reverse ile linki tekrar yazmak zorunda kalmadık. args içinde link ile alınan parametreler yazılır.