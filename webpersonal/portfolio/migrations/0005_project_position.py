# Generated by Django 3.1.4 on 2021-01-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210102_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cargo'),
        ),
    ]