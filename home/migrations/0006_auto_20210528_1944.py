# Generated by Django 3.2.3 on 2021-05-28 19:44

import blocks.fields
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0005_homepage_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='heading_streamfields',
            field=wagtail.core.fields.StreamField([('heading_title', blocks.fields.HeadingTitleBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_image',
            field=models.ForeignKey(blank=True, help_text='Set the image, this will be displayed below the page title.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
