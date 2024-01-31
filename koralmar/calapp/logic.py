from calapp.models import User
from django.shortcuts import redirect
from django.contrib import messages

def check_if_logged(request):
    """
    PAS UTILE POUR LE MOMENT...
    """
    try :
        user = User.objects.get(id=request.session['user_id'])
        return user
    except:
        messages.error(request, "Vous devez d'abord vous connecter...")
        return redirect('login')