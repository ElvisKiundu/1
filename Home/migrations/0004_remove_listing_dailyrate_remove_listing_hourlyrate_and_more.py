# Generated by Django 4.1 on 1980-01-01 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_listing_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='DailyRate',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='HourlyRate',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='WeeklyRate',
        ),
    ]
