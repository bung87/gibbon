# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.conf import settings



urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       # url(r'^$', 'views.home'),
                       url(r'^hello$', 'views.hello'),
)


if settings.DEBUG is True:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
        )
