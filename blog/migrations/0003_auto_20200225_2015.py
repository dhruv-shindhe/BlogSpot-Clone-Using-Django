# Generated by Django 3.0.2 on 2020-02-25 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200224_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 14, 45, 42, 502009, tzinfo=utc)),
        ),
    ]