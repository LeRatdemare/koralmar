import calapp.logic as logic
from calapp.models import Photo, User, MusicTheoryLesson, LogoVote
from calapp.forms import PhotoForm, UserForm, MusicTheoryLessonForm
from calapp.serializers import PhotoSerializer, UserSerializer, MusicTheoryLessonSerializer
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.urls import reverse
from django.forms import Form
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# from PIL import Image
# Create your views here.


def index(request):
    is_connected = True
    # Si l'utilisateur est connecté, il pourra ajouter des cours
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        is_connected = False
    context = { 'is_connected':is_connected }
    return render(request, 'calapp/index.html', context=context)

def events(request):
    is_connected = True
    # Si l'utilisateur est connecté, il pourra ajouter des cours
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        is_connected = False
    context = { 'is_connected':is_connected }
    return render(request, 'calapp/events.html', context=context)

def solfege(request):
    is_connected = True
    # Si l'utilisateur est connecté, il pourra ajouter des cours
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        is_connected = False
    
    mlts = MusicTheoryLesson.objects.all().order_by('lesson_day')
    context = { 'music_theory_lessons': mlts, 'is_connected':is_connected }

    if request.method == 'POST':
        form = MusicTheoryLessonForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('solfege'))
        else:
            context['form'] = form
            return render(request, 'calapp/solfege.html', context=context)
            
    context['form'] = MusicTheoryLessonForm()
    return render(request, 'calapp/solfege.html', context=context)

def choir(request):
    is_connected = True
    # Si l'utilisateur est connecté, il pourra ajouter des cours
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        is_connected = False
    context = { 'is_connected':is_connected }
    
    photos = Photo.objects.all()
    context['photos'] = photos
    return render(request, 'calapp/choir.html', context=context)

def contact_us(request):
    # On vérifie que l'utilisateur est connecté
    is_connected = True
    try :
        user = User.objects.get(id=request.session['user_id'])
    except:
        messages.error(request, "Vous devez d'abord vous connecter...")
        return redirect('login')
    context = { 'is_connected':is_connected }

    # Puis on regarde s'il vient de soummettre un formulaire
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('contact-us'))
        else:
            context['form'] = PhotoForm
            return render(request, 'calapp/contact_us.html', context=context)
    context['form'] = PhotoForm
    return render(request, 'calapp/contact_us.html', context=context)

def register(request):
    # Puis on regarde s'il vient de soummettre un formulaire
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        # On vérifie que le form soit valide
        if form.is_valid() :
            # On vérifie s'il y a un problème dans la saisie de l'utilisateur
            if User.objects.filter(login=form.cleaned_data['login']).exists():
                messages.error(request, "Il existe déjà un utilisateur avec ce login.")
                context = {'form': form}
                return render(request, 'calapp/register.html', context=context)
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, "Il existe déjà un utilisateur avec cet email.")
                context = {'form': form}
                return render(request, 'calapp/register.html', context=context)
            if request.POST['password'] != request.POST['confirmation']:
                messages.error(request, "Veuillez bien recopier votre mot de passe.")
                context = {'form': form}
                return render(request, 'calapp/register.html', context=context)
            # Si tout se passe bien, on enregistre l'inscription
            created_user = form.save(commit=False)
            created_user.password = make_password(request.POST['password'])
            created_user.save()
            request.session["user_id"] = created_user.id
            messages.success(request, "Compte créé avec succès, vous êtes maintenant connecté.")
            return redirect('index')
            
        else:
            messages.error(request, "Le form soumis n'est pas valide.")
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
            messages.error(request, "Le login n'existe pas.")
            return redirect('login')
        # On vérifie que le mot de passe est le bon
        if user.check_password(request.POST["password"]):
            request.session["user_id"] = user.id
            messages.success(request, "Vous êtes maintenant connecté.")
            return redirect('index')
        else:
            messages.error(request, "Le login et le mot de passe ne coïncident pas.")
            return redirect('login')
    # Si on vient seulement d'arriver sur la page et qu'on n'est pas connectés, on charge le formulaire
    context = {}
    return render(request, 'calapp/login.html', context=context)

def surveys(request: HttpRequest):
    # On vérifie que l'utilisateur est connecté
    is_connected = True
    user = None
    try:
        user = User.objects.get(id=request.session['user_id'])
    except:
        is_connected = False
    
    # Retreiving data from database
    logos = Photo.objects.filter(tag="LOGO")
    user_vote_logo_id = None
    votes = {}
    for logo in logos:
        votes[logo.id] = 0
    for vote in LogoVote.objects.all():
        votes[vote.logo.id] += 1
        if vote.user == user:
            user_vote_logo_id = vote.logo.id
            print("yeaaa")
    # Set context
    context = {
        'logos':logos,
        'votes':votes,
    }
    if is_connected:
        context['user'] = user
        context['user_vote_logo_id'] = user_vote_logo_id
    
    # Handle form response
    if request.method == 'POST':
        voted_logo = Photo.objects.get(id=request.POST['logoChoice'])
        # Check if user had already voted
        try:
            user_vote = LogoVote.objects.get(user=user)
            user_vote.logo = voted_logo
            user_vote.save()
        except LogoVote.DoesNotExist:
            LogoVote.objects.create(logo=voted_logo, user=user)
        return HttpResponseRedirect(reverse('surveys'))
        
    return render(request, 'calapp/surveys.html', context=context)

def error404(request):
    context = {}
    return render(request, "calapp/error404.html", context=context)


############################ LOGIC


def logout(request):
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    messages.info(request, "Vous êtes déconnecté.")
    return redirect('index')


############################ DATA


def get_music_theory_lessons(request):
    data = MusicTheoryLessonSerializer(MusicTheoryLesson.objects.all(), many=True).data
    return JsonResponse(data, safe=False)