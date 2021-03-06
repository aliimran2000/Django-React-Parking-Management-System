# Generated by Django 3.1.4 on 2020-12-26 15:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0037_auto_20201226_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Due_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 15, 5, 11, 458032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='Valid_To',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 15, 5, 11, 457035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='parking',
            name='In_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 15, 5, 11, 460026, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Payment_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 15, 5, 11, 458032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Registeration_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 15, 5, 11, 459029, tzinfo=utc)),
        ),
    ]
