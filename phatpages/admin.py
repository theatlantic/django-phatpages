from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import PhatPage


class PhatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))

    class Meta:
        model = PhatPage


class PhatPageAdmin(admin.ModelAdmin):
    form = PhatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'enable_comments', 'excerpt', 'template_name')}),
    )
    list_display = ('title', 'url')
    search_fields = ('title', 'url')


admin.site.register(PhatPage, PhatPageAdmin)
