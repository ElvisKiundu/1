# Generated by Django 4.1 on 2022-10-26 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_listing_listingimage_alter_listing_listinggallery_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='ListingGallery',
            new_name='ListingGallerys',
        ),
    ]
