# Generated by Django 3.2.4 on 2021-06-20 16:22

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0009_alter_blacklisteddomain_id'),
        ('blog', '0011_delete_blogpostcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.xtdcomment')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_comments', to='blog.blogpostpage')),
            ],
            options={
                'verbose_name': 'Blog Post Comment',
                'verbose_name_plural': 'Blog Post Comments',
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]
