from django.db import models
from django.conf import settings
from django.contrib import admin


class Book(models.Model):
    Book_name = models.CharField(max_length=150, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    Images = models.ImageField(upload_to=settings.MEDIA_ROOT,null=False)
    Author_name = models.CharField(max_length=150,null=False)
    Discription = models.CharField(max_length=900,null=True)

