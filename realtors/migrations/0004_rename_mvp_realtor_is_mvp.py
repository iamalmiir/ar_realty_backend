# Generated by Django 4.0.4 on 2022-05-29 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_rename_id_realtor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='mvp',
            new_name='is_mvp',
        ),
    ]
