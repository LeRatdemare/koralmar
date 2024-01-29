from django.shortcuts import render
from calapp.models import Photo
from calapp.forms import PhotoForm
import koralmar.dbinfos
# from PIL import Image

# Create your views here.


def index(request):
    return render(request, 'calapp/index.html')

def events(request):
    return render(request, 'calapp/events.html')

def solfege(request):
    return render(request, 'calapp/solfege.html')

def choir(request):
    return render(request, 'calapp/choir.html')

def contact_us(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Petite vérification pour bloquer les ajouts abusifs au début
            if koralmar.dbinfos.host == "localhost":
                form.save()
        else:
            context = {'form': form}
            return render(request, 'calapp/contact_us.html', context=context)
    context = {'form': PhotoForm}
    return render(request, 'calapp/contact_us.html', context=context)
