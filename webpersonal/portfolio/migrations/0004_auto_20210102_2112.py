# Generated by Django 3.1.4 on 2021-01-03 01:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210102_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owned_project',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha de Finalizacion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha de Inicio'),
        ),
    ]
