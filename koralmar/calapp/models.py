import os
from django.db import models
from django.dispatch import receiver
from django.core.exceptions import ValidationError
 
# creating a validator function
def validate_ensc_mail(value):
    if "@ensc.fr" in value:
        return value
    else:
        raise ValidationError("Vous devez vous inscrire avec une adresse ensc.")
    
class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, validators=[validate_ensc_mail])
    login = models.CharField(max_length=50)
    password = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Photo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/')
    date = models.DateTimeField(auto_now=True)

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=1500)
    datetime = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(Photo)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[{self.creator}] {self.datetime.time} ~ {self.description}"


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    try :
        if instance.photo:
            if os.path.isfile(instance.photo.path):
                os.remove(instance.photo.path)
    except:
        print("No file attached to photo")

@receiver(models.signals.pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    try :
        if not instance.pk:
            return False

        try:
            old_file = Photo.objects.get(pk=instance.pk).photo
        except Photo.DoesNotExist:
            return False

        new_file = instance.photo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except:
        print("A problem occured... Probably no file is attached to instance of Photo")