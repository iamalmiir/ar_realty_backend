# Generated by Django 4.0.4 on 2022-06-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]