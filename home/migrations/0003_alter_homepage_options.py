# Generated by Django 3.2.3 on 2021-05-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
    ]
