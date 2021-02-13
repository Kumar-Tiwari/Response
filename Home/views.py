from django.shortcuts import render
from Products_Details.models import Destination
from django.http import JsonResponse

def home_list(request):
    context=Destination.objects.all()[0:6]
    return render(request,'Home/home.html',{'products':context})

def home_detail_view(request,slug):
    data=Destination.objects.get(slug=slug)
    data2=data.additional_feature.all()
    if request.is_ajax() and request.method=='POST':
        rate=request.POST.get('val')
        data.ratings=rate
        data.save()
        return JsonResponse({'success':'True'},safe=False)
    return render(request,'Home/home_detail.html',{'data':data,'data2':data2})

def categoricalSorting(request, slug):
    posts=Destination.objects.filter(categories__slug=slug)
    return render(request, 'Home/categorial.html',{'posts':posts})

