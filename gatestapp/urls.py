from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template': 'homepage.html'}, name='homepage'),
    url(r'^books/', include('gatestapp.books.urls')),    
)
