from django.conf import settings

from django.template import loader, RequestContext

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

from .models import PhatPage


if hasattr(settings, 'PHATPAGES_DEFAULT_TEMPLATE'):
    DEFAULT_TEMPLATE = settings.PHATPAGES_DEFAULT_TEMPLATE
else:
    DEFAULT_TEMPLATE = 'staticpages/default.html'


# This view is called from PhatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching phatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def phatpage(request, url):
    """
    Public interface to the phat page view.

    """
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(PhatPage, url__exact=url)
    return render_fatpage(request, f)

# If a default Cache-Header Max-Age is defined in the settings
# Apply it to Fatpages
if hasattr(settings, 'CACHE_HEADER_MAX_AGE'):
    from django.views.decorators.cache import cache_control
    phatpage = cache_control(must_revalidate=True, max_age=settings.CACHE_HEADER_MAX_AGE)(phatpage)


@csrf_protect
def render_fatpage(request, f):
    """
    Internal interface to the fat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in fatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    c = RequestContext(request, {
        'fatpage': f,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, PhatPage, f.id)
    return response
