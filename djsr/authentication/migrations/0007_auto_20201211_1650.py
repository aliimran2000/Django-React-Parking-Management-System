# Generated by Django 3.1.3 on 2020-12-11 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20201211_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='CNIC',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='Phone_No',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Due_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 8, 16, 50, 20, 381025, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Valid_To',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 16, 50, 20, 380362, tzinfo=utc)),
        ),
    ]
