from django import forms
from calapp.models import Photo, User, Publication

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

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title','description', 'photos', 'creator')
        labels = {
            'title': 'Titre de la publication',
            'description': 'Description',
            'photos': 'Images',
            'creator': 'Auteur',
        }