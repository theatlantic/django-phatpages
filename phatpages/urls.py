from django.conf.urls.defaults import *

urlpatterns = patterns('phatpages.views',
    (r'^(?P<url>.*)$', 'phatpage'),
)
