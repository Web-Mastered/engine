from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeadingTitleBlock(blocks.RichTextBlock):
    """RichText heading block"""

    def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold", 
            "italic", 
            "link",
            "superscript",
            "subscript",
            "strikethrough",
        ]

    class Meta:
        template = "streams/heading_title_block.html"
        icon = "fa-header"
        label = "Title"

class HeadingSubtitleBlock(blocks.RichTextBlock):
    """RichText heading block"""

    def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold", 
            "italic", 
            "link",
            "superscript",
            "subscript",
            "strikethrough",
        ]

    class Meta:
        template = "streams/heading_subtitle_block.html"
        icon = "fa-header"
        label = "Subtitle"

class HeadingVariableBlock(blocks.RichTextBlock):
    """RichText heading block"""

    def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "bold", 
            "italic", 
            "link",
            "superscript",
            "subscript",
            "strikethrough",
        ]

    class Meta:
        template = "streams/heading_title_block.html"
        icon = "fa-header"
        label = "Title"

class WideImageBlock(blocks.StructBlock):
    """Images which take up the entire width of its parent"""

    align_options = (
        ("text-start", "Left"),
        ("text-center", "Centre"),
        ("text-end", "Right"),
    )

    image = ImageChooserBlock(required=True, help_text="Add an image.")
    alt_text = blocks.CharBlock(required=False,help_text="Displays this alternate text if the image cannot be displayed.")
    caption = blocks.RichTextBlock(features=['bold','italic','link','superscript','subscript','strikethrough'],required=False, help_text="Add an image caption.")
    caption_align = blocks.ChoiceBlock(label='Align the caption text.',required=False, choices=align_options)

    class Meta:
        template = "streams/wide_image_block.html"
        icon = "image"
        label = "Wide Image"

page_heading_blocks = StreamField(
    [
        ("heading_title", HeadingTitleBlock()),
        ("heading_subtitle", HeadingSubtitleBlock()),
        ("wide_image", WideImageBlock())
    ],
    null = True,
    blank = True,
    help_text = "Choose blocks to be shown at the top of the page."
)

class HomePageFields(models.Model):
    """HomePage field definitions"""

    heading_blocks = page_heading_blocks

    content_panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel("heading_blocks", classname=""),
            ],
            heading="Page Heading",
            classname="collapsible",
        ),
    ]

    class Meta:
        abstract = True


class FlexPageFields(models.Model):
    """FlexPage field definitions"""

    heading_blocks = page_heading_blocks

    content_panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel("heading_blocks", classname=""),
            ],
            heading="Page Heading",
            classname="collapsible",
        ),
    ]

    class Meta:
        abstract = True