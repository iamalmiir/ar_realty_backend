# Generated by Django 4.0.4 on 2022-07-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_alter_listing_pub_date'),
        ('contacts', '0005_remove_inquiry_listing_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='listing_details',
            field=models.ManyToManyField(blank=True, to='properties.listing'),
        ),
    ]
