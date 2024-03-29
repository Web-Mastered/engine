# Generated by Django 3.2.4 on 2021-06-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0005_auto_20210618_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name your category.', max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify posts by this category.', max_length=255)),
                ('image', models.ForeignKey(blank=True, help_text='Associate an image with this category.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Blog Post Category',
                'verbose_name_plural': 'Blog Post Categories',
                'ordering': ['name'],
            },
        ),
    ]
