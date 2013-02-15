# This file maps URL roots to applications.

from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views', # Factor out the common prefixes.
    url(r'^$', 'home', name='home'), # Optional named URL pattern allows you to tell them apart in templates.
)
