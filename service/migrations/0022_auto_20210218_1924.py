# Generated by Django 3.1.6 on 2021-02-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_middleimage_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertisewithtitleicon',
            name='content',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
