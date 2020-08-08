from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from app.models import *
# Create your views here.

def Home_page(request):
    return render(request,'home.html')


def category_page(request):
    return render (request,'category.html')