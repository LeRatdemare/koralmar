from django.contrib import admin
from calapp.models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'photo', 'date')

admin.site.register(Photo, PhotoAdmin)