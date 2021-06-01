from django.db import models


class User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.CharField(blank=True,max_length=100)

    birthday = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True) #cargar la fecha en la que se creo
    modified = models.DateTimeField(auto_now=True) # guarda la fecha en que se edito por ultima vez

    country = models.CharField(blank=True,max_length = 100)

    def __str__(self):
        "return email"
        return self.email