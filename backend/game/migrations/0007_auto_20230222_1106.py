# Generated by Django 2.2.28 on 2023-02-22 11:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_auto_20230206_0912'),
        ('game', '0006_gamescore_fir'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.Season'),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='score_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='status',
            field=models.CharField(default='Playing', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.League'),
        ),
    ]
