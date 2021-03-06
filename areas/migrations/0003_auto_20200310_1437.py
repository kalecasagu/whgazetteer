# Generated by Django 2.2.10 on 2020-03-10 14:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_auto_20191206_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='geojson',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
