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

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('login', 'password')
