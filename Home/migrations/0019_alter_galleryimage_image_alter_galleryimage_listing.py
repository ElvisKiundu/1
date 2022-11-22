# Generated by Django 4.1 on 2022-11-02 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_alter_galleryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='Image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='Listing',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.listing'),
        ),
    ]