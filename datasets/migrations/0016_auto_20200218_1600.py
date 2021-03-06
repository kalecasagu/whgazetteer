# Generated by Django 2.2.10 on 2020-02-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0015_dataset_uri_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='uri_base',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hit',
            name='authority',
            field=models.CharField(choices=[('tgn', 'Getty TGN'), ('dbp', 'DBpedia'), ('gn', 'Geonames'), ('wd', 'Wikidata'), ('core', 'WHG Spine'), ('whg', 'WHG')], max_length=12),
        ),
        migrations.AlterField(
            model_name='hit',
            name='query_pass',
            field=models.CharField(choices=[('pass1', 'Query pass 1'), ('pass2', 'Query pass 2'), ('pass3', 'Query pass 3')], max_length=12),
        ),
    ]
