# Generated by Django 3.2.4 on 2021-06-19 16:11

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpostcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogPostCategory'),
        ),
    ]
