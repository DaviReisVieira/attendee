# Generated by Django 5.1.2 on 2025-04-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0023_alter_recording_transcription_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='credential_type',
            field=models.IntegerField(choices=[(1, 'Deepgram'), (2, 'Zoom OAuth'), (3, 'Google Text To Speech'), (4, 'Gladia')]),
        ),
    ]
