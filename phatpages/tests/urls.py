from django.contrib import admin
from django.conf.urls.defaults import include, url, patterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
