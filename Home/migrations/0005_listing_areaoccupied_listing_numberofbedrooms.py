# Generated by Django 4.1 on 2022-10-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_remove_listing_dailyrate_remove_listing_hourlyrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='AreaOccupied',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Area Of Property'),
        ),
        migrations.AddField(
            model_name='listing',
            name='NumberOfBedrooms',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Number of Bedrooms'),
        ),
    ]