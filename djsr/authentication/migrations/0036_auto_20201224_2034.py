# Generated by Django 3.1.4 on 2020-12-24 15:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0035_auto_20201224_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Due_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 21, 15, 34, 37, 403332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Valid_To',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 15, 34, 37, 403332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='parking',
            name='In_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 15, 34, 37, 403332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Payment_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 15, 34, 37, 403332, tzinfo=utc)),
        ),
    ]