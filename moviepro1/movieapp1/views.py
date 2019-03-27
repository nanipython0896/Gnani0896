from django.shortcuts import render

from django.shortcuts import render
from .models import TeluguData,HindiData,EnglishData,UserData
from django.http.response import HttpResponse
def home(request):
    return render(request,'home.html')
def teluguview(request):
    tdata = TeluguData.objects.all()
    return render(request,'telugu.html',{'tdata':tdata})
def hindiview(request):
    hdata = HindiData.objects.all()
    return render(request,'hindi.html',{'hdata':hdata})
def englishview(request):
    edata = EnglishData.objects.all()
    return render(request,'english.html',{'edata':edata})
def user_view(request):
    if request.method =='POST':
        movie_name = request.POST.get('mname','')
        director_name = request.POST.get('dname','')
        hero_name = request.POST.get('hname','')
        heroine_name = request.POST.get('hename','')
        producer_name = request.POST.get('pname','')
        release_date = request.POST.get('rname','')
        udata = UserData(
            movie_name = movie_name,
            director_name= director_name,
            hero_name=hero_name,
            heroine_name=heroine_name,
            producer_name=producer_name,
            release_date=release_date,
        )
        udata.save()
        return render(request,'user.html',{'udata':udata})
    return render(request,'user.html')






















