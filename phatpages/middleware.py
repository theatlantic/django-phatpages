import importlib

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

from .models import PhatPage


class PhatpageFallbackMiddleware(MiddlewareMixin):

    @property
    def phatpage_view(self):
        try:
            view_settings_str = settings.PHATPAGE_VIEW
        except AttributeError:
            raise ImproperlyConfigured("You must define a 'PHATPAGE_VIEW' variable in your settings before using the PhatpageFallbackMiddleware")
        module_str, view_str = view_settings_str.rsplit(".", 1)
        module = importlib.import_module(module_str)
        view = getattr(module, view_str)
        if hasattr(view, 'as_view'):
            return view.as_view()
        else:
            return view

    def process_response(self, request, response):
        if response.status_code != 404:
            return response  # No need to check for a fatpage for non-404 responses.
        try:
            page = get_object_or_404(PhatPage, url=request.path_info, site_id=settings.SITE_ID)
            response = self.phatpage_view(request, page)
            if hasattr(response, 'render'):
                response.render()
            return response

        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
