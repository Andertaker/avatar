# -*- coding: utf-8 -*-
import os
import json
from StringIO import StringIO

from PIL import Image
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea, CharField, Select
from django.template import RequestContext, Context
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile

from models import *
from img_tools import ImgTools  #img_tools.__init__.py


FILE_LIMIT = 1 #Mb
FILE_LIMIT_BYTES = FILE_LIMIT * 1024 * 1024









class UserIndexView(generic.ListView):
    model = User
    template_name = 'users_list.html'





class UserForm(forms.ModelForm):
    #error_css_class = 'error'
    #required_css_class = 'required'
    username = forms.CharField(label="Логин", required=True, widget=forms.TextInput(attrs={'required': "required"}))
    email = forms.EmailField(label="E-mail", required=True, widget=forms.TextInput(attrs={'required': "required"}))
    password1 = forms.CharField(label="Новый пароль", required=False, widget=forms.PasswordInput)
    #password2 = forms.CharField(label="Подтверждение", required=True, widget=forms.PasswordInput)
    '''
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            'username': forms.TextInput(attrs={'required': "required"}),
            'email': forms.TextInput(attrs={'required': "required"}),
            'password': forms.PasswordInput(attrs={'required': "required"}),
        }
    '''
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile





def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)

        if form.is_valid() and len(form.errors) == 0:
            
            user = form.save(commit=False)
            user.is_staff = True    #чтоб в админку попасть (для теста)
            
            if form.cleaned_data["password1"]:
                user.set_password(form.cleaned_data["password1"])
            
            user.save()
            
            
        
    else:
        form = UserForm(instance=user)
    
    
    context = RequestContext(request, {"form": form, "selected_user": user})
    return render(request, 'user_edit.html', context)










def avatar_upload(request, pk):
    response = HttpResponse(mimetype='application/json')
    result = {"status": "error"}
    form = ProfileForm(request.POST, request.FILES)
    
    #print dir(request.FILES["avatar"])
    #print request.FILES["avatar"].size
    
    user = get_object_or_404(User, pk=pk)
    profile = Profile()
    profile.user = user
    

    if form["avatar"].errors:
        result["err_message"] = form["avatar"].errors[0]
        response.write(json.dumps(   result   ))
        return response
    
    f = form.cleaned_data["avatar"]
    if f.size > FILE_LIMIT_BYTES:
        result["err_message"] = "Загрузите файл меньше чем %s Mb" % + FILE_LIMIT
        response.write(json.dumps(   result   ))
        return response
 
    "получаем аватар и храним его ввиду строки"
    s = f.read()
    im = Image.open(StringIO(s))
    #print im.format, im.size, im.mode
    tools = ImgTools()  #img_tools.__init__.py
    im = tools.make_avatar(im)
    str_object = StringIO()
    im.save(str_object, 'JPEG')
    content = str_object.getvalue() 
    str_object.close()

    
    file_name = profile.avatar.field.upload_to + "/" + str(user.id) + ".jpg"
    profile.avatar.name = file_name
    "удаляем старый файл"
    if os.path.isfile(profile.avatar.path):
        os.remove(profile.avatar.path)
    "сохраняем новый (сохранится при сохранении профиля)"
    profile.avatar.save(file_name, ContentFile(content), save=False)

    
    profile.save()
    result["status"] = "success"
    result["avatar_url"] = profile.avatar.url
   

    response.write(json.dumps(   result   ))
    return response
    
    
    #return HttpResponseRedirect(reverse('user_edit', kwargs={"pk": user.id}))







