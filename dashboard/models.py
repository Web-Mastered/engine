from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import HelpPanel

# Create your models here.

@register_setting(icon='help')
class AboutEngine(BaseSetting):
    """
    This class displays a HelpPanel in a newly created settings tab "About Engine"
    the HelpPanel displays various information regarding Engine.
    """
    panels = [
        HelpPanel(
            template='engine/index.html',
        )
    ]

    class Meta:
        """ Meta AboutEngine """
        verbose_name = 'About Engine'