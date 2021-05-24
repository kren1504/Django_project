from django.db import models


class Users(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.CharField(blank=True,max_length=100)

    birthday = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True) #cargar la fecha en la que se creo
    modified = models.DateTimeField(auto_now=True) # guarda la fecha en que se edito por ultima vez
