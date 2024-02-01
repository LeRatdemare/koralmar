from calapp.models import User
from django.shortcuts import redirect
"""
Fichier non généré de base par le framework Django. Stock des fonctions de logique
"""
from django.contrib import messages
import requests
import json

spotify_client_id = ""
spotify_client_secret = ""
token = ""
spotify_prefix = "https://api.spotify.com"
headers = {'api-key': token}

def getSpotifyAccessToken():
    pass

def getSpotifyPlaylist(id):
    url = spotify_prefix + "/v1/me/playlists"


############## USELESS Yet

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
