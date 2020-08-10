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