# Generated by Django 4.0.4 on 2022-07-08 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_listing_pub_date_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 8, 11, 5, 5, 158307)),
        ),
    ]