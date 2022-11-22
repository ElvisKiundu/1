# Generated by Django 4.1 on 2022-10-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_listinggallery2_listing_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(default=None, upload_to='')),
                ('Name', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='Gallery',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='ListingGallery',
        ),
        migrations.DeleteModel(
            name='ListingGallery2',
        ),
    ]
