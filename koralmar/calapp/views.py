from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'calapp/index.html')


def events(request):
    return render(request, 'calapp/events.html')


def solfege(request):
    return render(request, 'calapp/solfege.html')


def contact_us(request):
    return render(request, 'calapp/contact_us.html')
