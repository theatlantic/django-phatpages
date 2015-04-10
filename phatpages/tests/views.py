from django.http import HttpResponse
from django.views.generic import View


def view_function(request, static_page):
    html = "<html><body>view_function: %s</body></html>" % static_page.content
    return HttpResponse(html)


class ViewClass(View):

    def get(self, request, static_page):
        html = "<html><body>ViewClass: %s</body></html>" % static_page.content
        return HttpResponse(html)
