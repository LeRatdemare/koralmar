from django.contrib import admin
from calapp.models import Photo, User, MusicTheoryLesson

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'photo', 'date')
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'login', 'password', 'profile_picture')
class MusicTheoryLessonAdmin(admin.ModelAdmin):
    list_display = ('canva_link', 'description', 'lesson_day')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MusicTheoryLesson, MusicTheoryLessonAdmin)