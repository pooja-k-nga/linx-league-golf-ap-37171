# Generated by Django 2.2.28 on 2023-01-13 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('when', models.DateTimeField(blank=True, null=True)),
                ('course_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('course_address', models.CharField(blank=True, max_length=255, null=True)),
                ('players', models.ManyToManyField(blank=True, related_name='players_added_as_friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_who_is_scheduling', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'League',
                'verbose_name_plural': 'Leagues',
            },
        ),
    ]
