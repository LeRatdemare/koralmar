from django.db import models

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
