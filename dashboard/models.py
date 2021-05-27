from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import HelpPanel

# Create your models here.

@register_setting(icon='help')
class AboutEngine(BaseSetting):
    panels = [
        HelpPanel(
            template='engine/index.html',
        )
    ]

    class Meta:
        verbose_name = 'About Engine'