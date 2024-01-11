from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('this is home page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is about us page')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is services page')

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')

def product(request):
    return render(request, 'product.html')
    # return HttpResponse('this is product page')
