# Generated by Django 3.1.6 on 2021-02-19 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='catagory',
            new_name='blog_catagory',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='blog_content',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='blog_image',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='owners',
            new_name='blog_owners',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='share',
            new_name='blog_share',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='time',
            new_name='blog_time',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='blog_title',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='views',
            new_name='blog_views',
        ),
    ]
