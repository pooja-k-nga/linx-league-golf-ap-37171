# Generated by Django 2.2.28 on 2023-02-06 09:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_auto_20230203_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfcourse',
            name='hdcp',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='golfcourse',
            name='hole',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='golfcourse',
            name='par',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='golfcourse',
            name='red_distance',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
