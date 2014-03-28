# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf import settings



urlpatterns = patterns('gibbon',
                       # url(r'^admin/', include(admin.site.urls)),
                       # url(r'^$', 'views.home'),
                       url(r'^$', 'views.hello'),
                       url(r'^create_event', 'views.create_event'),
                       url(r'^list_event', 'views.list_event'),
)


if settings.DEBUG is True:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
        )
