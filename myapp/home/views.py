from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('this is home page')

def about(request):
    return HttpResponse('this is about us page')

def servers(request):
    return HttpResponse('this is servers page')

def contact(request):
    return HttpResponse('this is contact page')
