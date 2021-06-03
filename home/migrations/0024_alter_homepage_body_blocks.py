# Generated by Django 3.2.3 on 2021-06-03 10:30

import blocks.fields
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_homepage_body_blocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_blocks',
            field=wagtail.core.fields.StreamField([('body_title', blocks.fields.BodyTitleBlock()), ('body_paragraph', blocks.fields.BodyParagraphBlock()), ('body_wide_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add an image.', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(default='This is an image.', help_text='Displays this alternate text if the image cannot be displayed.', required=False)), ('caption', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'superscript', 'subscript', 'strikethrough'], help_text='Add an image caption.', required=False)), ('caption_align', wagtail.core.blocks.ChoiceBlock(choices=[('text-start', 'Left'), ('text-center', 'Centre'), ('text-end', 'Right')], label='Align the caption text.', required=False))])), ('body_image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add an image.', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(default='This is an image.', help_text='Displays this alternate text if the image cannot be displayed.', required=False)), ('caption', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'superscript', 'subscript', 'strikethrough'], help_text='Add an image caption.', required=False)), ('text', blocks.fields.BodyParagraphBlock(help_text='Add some text to display beside the image.', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('image-left', 'Image - Text'), ('image-right', 'Text - Image')], label='Align the image and text.', required=False))]))], blank=True, help_text='Choose blocks to be shown in the body.', null=True),
        ),
    ]
