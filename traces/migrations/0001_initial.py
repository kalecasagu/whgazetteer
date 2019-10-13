# Generated by Django 2.2.4 on 2019-10-12 15:09

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0007_auto_20191012_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('src_id', models.CharField(max_length=2044)),
                ('context', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('uri', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('trace_type', models.CharField(default='Annotation', max_length=20)),
                ('creator', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('motivation', models.CharField(max_length=20)),
                ('dataset', models.ForeignKey(db_column='dataset', on_delete=django.db.models.deletion.CASCADE, related_name='traces', to='datasets.Dataset', to_field='label')),
            ],
            options={
                'db_table': 'traces',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TraceTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('title', models.CharField(max_length=255)),
                ('types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('person', 'Person'), ('dataset', 'Dataset'), ('event', 'Event'), ('journey', 'Journey'), ('work', 'Work')], max_length=30), blank=True, null=True, size=None)),
                ('description', models.TextField()),
                ('trace_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='traces.Trace')),
            ],
            options={
                'db_table': 'trace_target',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TraceBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('title', models.CharField(max_length=255)),
                ('when', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('relation', models.CharField(choices=[('subject', 'Subject'), ('waypoint', 'Waypoint'), ('birthplace', 'Birth place'), ('deathplace', 'Death place'), ('resided', 'Resided'), ('taught', 'Taught'), ('enlightened', 'Enlightened'), ('findspot', 'Findspot'), ('ruled', 'Ruled')], max_length=20)),
                ('trace_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='bodies', to='traces.Trace')),
            ],
            options={
                'db_table': 'trace_body',
                'managed': True,
            },
        ),
        migrations.AddIndex(
            model_name='trace',
            index=models.Index(fields=['dataset'], name='traces_dataset_053971_idx'),
        ),
    ]