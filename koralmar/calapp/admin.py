from django.contrib import admin
from calapp.models import Photo, User

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'photo', 'date')
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'login', 'password', 'profile_picture')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(User, UserAdmin)