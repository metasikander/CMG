from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin.py:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CMG.views.home', name='home'),
    # url(r'^CMG/', include('CMG.foo.urls')),

    # Uncomment the admin.py/doc line below to enable admin.py documentation:
    #url(r'^admin.py/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin.py:
    url(r'^admin/', include(admin.site.urls)),
)
