# Generated by Django 4.1 on 2022-09-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Owner',
            field=models.IntegerField(default=None, verbose_name='Listing Owner'),
        ),
    ]
