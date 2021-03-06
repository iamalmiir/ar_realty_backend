# Generated by Django 4.0.4 on 2022-07-18 20:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInquiry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(max_length=255)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.UUIDField(blank=True, null=True)),
            ],
        ),
    ]
