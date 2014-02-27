# -*- coding: utf-8 -*-


from django.contrib.auth.models import User
from django.db import models






class Profile(models.Model):
    #groups = models.OneToOneField(Avatar, blank=True)
    avatar = models.ImageField(upload_to="avatars")
    user = models.OneToOneField(User, primary_key=True)

    class Meta:
        """
        Упорядочивать выборки по username, если не задан другой порядок
        """
        ordering = ["user__username"]


    
    