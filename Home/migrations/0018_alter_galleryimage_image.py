# Generated by Django 4.1 on 2022-10-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_galleryimage_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='Image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
