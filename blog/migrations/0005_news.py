# Generated by Django 3.1.6 on 2021-02-19 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=5000)),
                ('time', models.DateTimeField(auto_now=True)),
                ('share', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('owners', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='wesiteblog/images')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.catagory')),
            ],
        ),
    ]
