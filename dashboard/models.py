from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import HelpPanel

# Create your models here.

@register_setting(icon='placeholder')
class AboutEngine(BaseSetting):
    panels = [
        HelpPanel(
            template='engine/index.html',
        )
    ]

    def change_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            extra_context = extra_context or {}
            extra_context['readonly'] = True

        return super(AboutEngine, self).change_view(request, object_id, extra_context=extra_context)

    class Meta:
        verbose_name = 'About Engine'