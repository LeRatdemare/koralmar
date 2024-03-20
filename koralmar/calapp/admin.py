from django.contrib import admin
from calapp.models import Photo, User, MusicTheoryLesson, LogoVote

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'photo', 'date', 'tag')
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'login', 'password', 'profile_picture')
class MusicTheoryLessonAdmin(admin.ModelAdmin):
    list_display = ('canva_link', 'description', 'lesson_day')
class LogoVoteAdmin(admin.ModelAdmin):
    list_display = ('logo', 'user')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MusicTheoryLesson, MusicTheoryLessonAdmin)
admin.site.register(LogoVote, LogoVoteAdmin)