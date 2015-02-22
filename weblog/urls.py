from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Blog URLs
    url(r'^.*$', include('blog.urls')),
)
