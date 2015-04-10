from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.sites.models import Site

from phatpages.models import PhatPage


middleware_classes = settings.MIDDLEWARE_CLASSES + ('phatpages.middleware.PhatpageFallbackMiddleware', )


@override_settings(MIDDLEWARE_CLASSES=middleware_classes,
                   ROOT_URLCONF="phatpages.tests.urls",
                   SITE_ID=42)
class TestPhatpageViewFunction(TestCase):

    def setUp(self, *args, **kwargs):
        site = Site.objects.create(id=42, domain="example.com", name="example")
        PhatPage.objects.create(site=site, url="test-url", title="title", content="content")

    @override_settings(PHATPAGE_VIEW="phatpages.tests.views.view_function")
    def test_404s_still_work(self):
        rsp = self.client.get('not-a-url')
        self.assertEqual(rsp.status_code, 404)

    @override_settings(PHATPAGE_VIEW="phatpages.tests.views.view_function")
    def test_view_function(self):
        rsp = self.client.get('test-url')
        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp.content, '<html><body>view_function: content</body></html>')

    @override_settings(PHATPAGE_VIEW="phatpages.tests.views.ViewClass")
    def test_view_class(self):
        rsp = self.client.get('test-url')
        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp.content, '<html><body>ViewClass: content</body></html>')
