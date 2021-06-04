from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import EditHandler, FieldRowPanel, HelpPanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

@register_setting
class WebsiteSettings(BaseSetting):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Choose an image for the site logo. This logo will be displayed at various places around the website."
    )

    site_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Site icons are what you see in browser tabs and bookmark bars, please upload a square image."
    )

    look_and_feel_panels = [
        FieldRowPanel([
            ImageChooserPanel("logo"),
            ImageChooserPanel("site_icon")
        ], heading="Branding"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(look_and_feel_panels, heading="Look & Feel"),
        # ObjectList(look_and_feel_panels, heading="Another Tab"), # More tabs can be added like this...
    ])


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
