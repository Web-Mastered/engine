# Generated by Django 3.2.3 on 2021-05-28 15:10

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='page_title',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Set the title, this will be displayed at the top of the page.', max_length=255, null=True),
        ),
    ]
