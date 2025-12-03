from django.urls import re_path as url

from django.contrib import admin
from django.urls import path, include
from django.conf import  settings 
from django.conf.urls.static import static
from .views import manifest, service_worker, offline

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    url(r'^serviceworker\.js$', service_worker, name='serviceworker'),
    url(r'^manifest\.json$', manifest, name='manifest'),
    url('^offline/$', offline, name='offline')

]