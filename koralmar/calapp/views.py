import calapp.logic as logic
from calapp.models import Photo, User
from calapp.forms import PhotoForm, UserForm
from django.shortcuts import render, redirect
from django.forms import Form
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# from PIL import Image

# Create your views here.


def index(request):    
    context = { }
    return render(request, 'calapp/index.html', context=context)

def events(request):
    context = { }
    return render(request, 'calapp/events.html', context=context)

def solfege(request):
    context = { }
    return render(request, 'calapp/solfege.html', context=context)

def choir(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'calapp/choir.html', context=context)

def contact_us(request):
    # On vérifie que l'utilisateur est connecté
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        messages.error(request, "Vous devez d'abord vous connecter...")
        return redirect('login')

    # Puis on regarde s'il vient de soummettre un formulaire
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
        else:
            context = {'form': form}
            return render(request, 'calapp/contact_us.html', context=context)
    context = { 'form': PhotoForm }
    return render(request, 'calapp/contact_us.html', context=context)

def register(request): # A TRAVAILLER --> Verification et enregistrement des données
    # Puis on regarde s'il vient de soummettre un formulaire
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        # On vérifie que le form soit valide
        if form.is_valid() :
            form.save()
            messages.success(request, "Compte créé avec succès.")
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'calapp/register.html', context=context)
    context = { 'form': UserForm }
    return render(request, 'calapp/register.html', context=context)

def login(request):
    # Si l'utilisateur est déjà connecté on le redirige à l'accueil
    try:
        user_id = request.session['user_id']
        messages.warning(request, "Vous êtes déjà connecté...")
        return redirect('index')
    except:
        pass

    # Sinon on regarde s'il a tenté de se connecter
    if request.method == 'POST':
        # On essaie de récupérer son login
        try:
            user = User.objects.get(login=request.POST["login"])
        except User.DoesNotExist:
            messages.error(request, "Login does not exist.")
            return redirect('login')
        # On vérifie que le mot de passe est le bon
        if user.check_password(request.POST["password"]):
            request.session["user_id"] = user.id
            messages.success(request, "You have been successfully connected.")
            return redirect('index')
        else:
            messages.error(request, "Login and password do not match")
            return redirect('login')
    # Si on vient seulement d'arriver sur la page et qu'on n'est pas connectés, on charge le formulaire
    context = { }
    return render(request, 'calapp/login.html', context=context)

############################ LOGIC

def logout(request):
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    messages.info(request, "Vous êtes déconnecté.")
    return redirect('index')