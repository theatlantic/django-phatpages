from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

class FatPage(models.Model):
	url = models.CharField(_('URL'), max_length=100, db_index=True)
	title = models.CharField(_('title'), max_length=200)
	content = RichTextField(null=True, blank=True)
	enable_comments = models.BooleanField(_('enable comments'))
	template_name = models.CharField(_('template name'), max_length=70, blank=True,
									 help_text=_("Example: 'staticpages/contact_page.html'. If this isn't provided, the system will use 'the default."))

	registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))

	class Meta:
		db_table = 'django_flatpage'
		verbose_name = _('static page')
		verbose_name_plural = _('static pages')
		ordering = ('url',)
		app_label = 'staticpages'

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url
