# Generated by Django 3.1.4 on 2021-01-03 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201228_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicacion'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicacion'),
        ),
    ]
