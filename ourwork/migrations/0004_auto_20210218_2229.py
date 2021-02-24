# Generated by Django 3.1.6 on 2021-02-18 16:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ourwork', '0003_remove_headbanner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='headbanner',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectimage', models.ImageField(upload_to='ourwork/projectimage')),
                ('projecticon', models.ImageField(upload_to='ourwork/projecticon')),
                ('projectTitle', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=5000)),
                ('projectsource', models.ImageField(upload_to='ourwork/projectsource')),
                ('catagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourwork.ourwork_cat')),
            ],
        ),
    ]
