# Generated by Django 3.2 on 2022-09-19 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectivity',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 12, 13, 23, 141923)),
        ),
    ]