from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.sites.models import Site

from phatpages.models import PhatPage


@override_settings(SITE_ID=42)
class TestPhatpageViewFunction(TestCase):

    def setUp(self, *args, **kwargs):
        site = Site.objects.create(id=42, domain="phatpages.com", name="phatpages")
        PhatPage.objects.create(site=site, url="test-url", title="title", content="content")

    @override_settings(PHATPAGE_VIEW="views.view_function")
    def test_404s_still_work(self):
        rsp = self.client.get('not-a-url')
        self.assertEqual(rsp.status_code, 404)

    @override_settings(PHATPAGE_VIEW="views.view_function")
    def test_view_function(self):
        rsp = self.client.get('test-url')
        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp.content, b'<html><body>view_function: content</body></html>')

    @override_settings(PHATPAGE_VIEW="views.ViewClass")
    def test_view_class(self):
        rsp = self.client.get('test-url')
        self.assertEqual(rsp.status_code, 200)
        self.assertEqual(rsp.content, b'<html><body>ViewClass: content</body></html>')
