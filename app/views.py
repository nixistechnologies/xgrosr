from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from app.models import *
# Create your views here.

def Home_page(request):
    return render(request,'home.html')

def listPage(request):
    return render(request,'listPage.html')

def category_page(request):
    c = Category.objects.all()
    return render (request,'category.html',{'category':c})

def list_page(request,d):
    # cat = Category.objects.get(id=d)
    # cat1 = Category.objects.filter(category=d)
    print(d)
    cat1 = Product.objects.filter(category_id=d)
    # print(cat1)
    for i in cat1.values():
        print(i)
    return render(request,'listPage.html',{"data":cat1})
    cat1 = Product.objects.filter(category=d)
    print(cat1)
    return render(request,'listPage.html',{'product':cat1})
