# Generated by Django 2.2.28 on 2023-02-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_gamescore_hole'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='fir',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
