import os
from django.db import models
from django.dispatch import receiver

class User(models.Model):
    name = models.CharField(max_length=255)

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
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Photo.objects.get(pk=instance.pk).file
    except Photo.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)