# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_task_avatar.views.home', name='home'),
    # url(r'^test_task_avatar/', include('test_task_avatar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    
    
    url(r'^$', views.UserIndexView.as_view(), name='users'),
    url(r'user/(?P<pk>\d+)/edit', views.user_edit, name='user_edit'),
    
    url(r'avatar_upload/(?P<pk>\d+)/', views.avatar_upload, name='avatar_upload'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)





if settings.DEBUG:
    urlpatterns = patterns('',
                           
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),     
                                  
    url(r'', include('django.contrib.staticfiles.urls')),
    
) + urlpatterns


