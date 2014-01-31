from django.conf.urls import patterns, include, url

from loteria_django.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^loteria/$', show_card),
    # Examples:
    # url(r'^$', 'loteria_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
