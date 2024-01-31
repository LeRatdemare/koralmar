from django import forms
from calapp.models import Photo, User

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'owner', 'photo')
        labels = {
            'name': "Titre de l'image",
            'owner': "Propriétaire",
            'photo': "Image",
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'login', 'profile_picture')
        labels = {
            'name': 'Nom',
            'email': 'Adresse mail (ensc)',
            'login': 'Login',
            'profile_picture': 'Photo de profil',
        }
