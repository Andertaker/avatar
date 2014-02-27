# -*- coding: utf-8 -*-



from django.db import models

from django.contrib import admin
from models import *




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)





admin.site.register(Profile, ProfileAdmin)


