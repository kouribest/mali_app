#coding: utf-8 
"""mali_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mali_project.views import *
from mali_project.crud_view.crud_view import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^$', home, name='home'),
    url(r'^addform$', addform, name='addform'),
    url(r'^scan$', scanView, name='scanView'),
    url(r'^search/(?P<record_id>\w+$)', RecordFinder.as_view(), name='record_lookup'),
    url(r'^approbe/(?P<form_id>\w{6}$)',approbeForm, name='approbe_form'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^list_registration', ListRecord.as_view(), name='record_list'),
    url(r'^delete_form/(?P<pk>\w{6}$)', DeleteRecord.as_view(), name='delete_record'),
    url(r'^update_registration/(?P<pk>\w{6}$)', UpdateForm.as_view(), name='update_registration'),
    url(r'^about/', about, name='about'),
    url(r'^stats/', StatsView.as_view(), name='stats'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
