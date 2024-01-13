from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_instance = Contact(
            name=name, email=email, subject=subject, message=message,date = datetime.today())
        contact_instance.save()
        messages.success(request, "message is sent!")
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')


def product(request):
    return render(request, 'product.html')
    # return HttpResponse('this is product page')
