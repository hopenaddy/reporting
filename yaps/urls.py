from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'reporting.views.index', ),
    # url(r'^blog/', include('blog.urls')),

    url(r'^result/', 'reporting.views.result'),
)
