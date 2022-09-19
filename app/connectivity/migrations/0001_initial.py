# Generated by Django 3.2 on 2022-09-19 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('description', models.CharField(max_length=255)),
                ('is_accessible', models.BooleanField(default=False)),
                ('is_enabled', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 12, 11, 42, 168218))),
                ('update_counter', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
