from rest_framework import serializers
from calapp.models import *

class MusicTheoryLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicTheoryLesson
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'login', 'profile_picture')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'