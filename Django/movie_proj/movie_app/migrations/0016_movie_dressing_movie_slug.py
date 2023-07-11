# Generated by Django 4.1 on 2022-09-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_remove_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dressing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.dressingroom'),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
