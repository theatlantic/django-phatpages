from django.conf.urls.defaults import *

urlpatterns = patterns('fatpages.views',
    (r'^(?P<url>.*)$', 'fatpage'),
)
