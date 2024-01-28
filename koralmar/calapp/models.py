from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)

class Photo(models.Model):
    name = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='photos/')
    date = models.DateTimeField()

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=1500)
    datetime = models.DateTimeField()
    photos = models.ManyToManyField(Photo)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[{self.creator}] {self.datetime.time} ~ {self.description}"
